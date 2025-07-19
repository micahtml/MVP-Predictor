
import streamlit as st
import pandas as pd
import plotly.graph_objs as go

@st.cache_data
def fetch_data(season: int) -> pd.DataFrame:
    url = f"https://www.basketball-reference.com/leagues/NBA_{season}_totals.html"
    try:
        df = pd.read_html(url)[0]
    except Exception as e:
        st.error(f"Failed to fetch data: {e}")
        return pd.DataFrame()
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df.drop("Rk", axis=1, inplace=True)
    df.rename(columns={"Unnamed: 1": "Player"}, inplace=True)
    df.drop(df.tail(2).index, inplace=True)
    df.drop_duplicates(inplace=True)
    df.dropna(how="all", inplace=True)

    numeric_cols = [
        "G", "MP", "FG", "FGA", "3P", "3PA", "FT", "FTA", "ORB", "DRB",
        "TRB", "AST", "STL", "BLK", "TOV", "PF", "PTS"
    ]
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")
    return df

def calculate_mvp_score(df: pd.DataFrame, weights: dict) -> pd.DataFrame:
    df["MVP_Score"] = (
        weights["PTS"] * df["PTS"] +
        weights["TRB"] * df["TRB"] +
        weights["AST"] * df["AST"] +
        weights["G"] * df["G"] +
        weights["FGA"] * df["FGA"]
    )
    mvp_df = (
        df[["Player", "Pos", "Age", "G", "MP", "PTS", "TRB", "AST", "FGA", "MVP_Score"]]
        .sort_values("MVP_Score", ascending=False)
        .head(5)
    )
    return mvp_df

def plot_top_candidates(mvp_df: pd.DataFrame):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=mvp_df["Player"],
        y=mvp_df["MVP_Score"],
        name="MVP Score",
        marker_color='darkblue'
    ))
    fig.update_layout(title="Top 5 NBA MVP Candidates (Performance-Based)",
                      xaxis_title="Player", yaxis_title="MVP Score")
    return fig

def main():
    st.title("🏀 NBA MVP Predictor (Advanced)")
    st.markdown("Analyze NBA season stats and predict the top MVP candidates using customizable scoring.")

    season = st.slider("Select NBA Season", 2000, 2025, 2025)
    raw_df = fetch_data(season)

    if not raw_df.empty:
        clean_df = clean_data(raw_df)

        # Advanced Filters
        pos_options = clean_df["Pos"].unique().tolist()
        selected_pos = st.multiselect("Filter by Position", pos_options, default=pos_options)

        age_min, age_max = int(clean_df["Age"].min()), int(clean_df["Age"].max())
        selected_age = st.slider("Select Age Range", age_min, age_max, (age_min, age_max))

        filtered_df = clean_df[
            clean_df["Pos"].isin(selected_pos) &
            clean_df["Age"].between(selected_age[0], selected_age[1])
        ]

        st.sidebar.header("Scoring Weights")
        weights = {
            "PTS": st.sidebar.slider("Weight for Points", 0.0, 1.0, 1.0, 0.1),
            "TRB": st.sidebar.slider("Weight for Rebounds", 0.0, 1.0, 1.0, 0.1),
            "AST": st.sidebar.slider("Weight for Assists", 0.0, 1.0, 1.0, 0.1),
            "G": st.sidebar.slider("Weight for Games Played", 0.0, 1.0, 1.0, 0.1),
            "FGA": st.sidebar.slider("Weight for FGA", 0.0, 1.0, 1.0, 0.1),
        }

        mvp_df = calculate_mvp_score(filtered_df, weights)

        st.subheader(f"Top 5 MVP Candidates - {season} Season")
        st.dataframe(mvp_df.reset_index(drop=True))
        st.plotly_chart(plot_top_candidates(mvp_df), use_container_width=True)

if __name__ == "__main__":
    main()
