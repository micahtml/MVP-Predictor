import pandas as pd
import plotly.graph_objs as go

# Define the URL for the NBA season stat leaders data
url = "https://www.basketball-reference.com/leagues/NBA_2025_totals.html"

# Use pandas to read the HTML table into a DataFrame
# df = pd.read_html(url)[0]

# # Remove the "Rk" column
# df.drop("Rk", axis=1, inplace=True)

# # Rename the "Unnamed: 1" column to "Player"
# df.rename(columns={"Unnamed: 1": "Player"}, inplace=True)

# # Remove the last 2 rows (total and league average)
# df.drop(df.tail(2).index, inplace=True)

# # Remove duplicates
# df.drop_duplicates(inplace=True)

# # Remove any rows where all columns are empty
# df.dropna(how="all", inplace=True)

# Convert the relevant columns to numeric data type
numeric_cols = [
    "G",
    "MP",
    "FG",
    "FGA",
    "3P",
    "3PA",
    "FT",
    "FTA",
    "ORB",
    "DRB",
    "TRB",
    "AST",
    "STL",
    "BLK",
    "TOV",
    "PF",
    "PTS",
]
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

# Select the top 5 MVP candidates based on points, rebounds, assists, games played, and minutes played
df["MVP_Score"] = df["PTS"] + df["TRB"] + df["AST"] + df["G"] + df["FGA"]
mvp_df = (
    df[["Player", "Pos", "Age", "G", "MP", "PTS", "TRB", "AST", "MVP_Score"]]
    .sort_values("MVP_Score", ascending=False)
    .head(5)
)

print("Top 5 Candidates in NBA 2024-25 season (Performance based)")
print(mvp_df)

# Create a bar chart of the top 5 MVP candidates with their stats
fig = go.Figure()
fig.add_trace(go.Bar(name="Minutes Played", x=mvp_df["Player"], y=mvp_df["MP"]))
fig.add_trace(go.Bar(name="Points", x=mvp_df["Player"], y=mvp_df["PTS"]))
fig.add_trace(go.Bar(name="Rebounds", x=mvp_df["Player"], y=mvp_df["TRB"]))
fig.add_trace(go.Bar(name="Assists", x=mvp_df["Player"], y=mvp_df["AST"]))
fig.add_trace(go.Bar(name="Games Played", x=mvp_df["Player"], y=mvp_df["G"]))
# fig.add_trace(go.Bar(name='Field Goal Average', x=mvp_df['Player'], y=mvp_df['FGA']))


fig.update_layout(
    title="Top 5 MVP Candidates in NBA 2024-25 Season (Performance based)",
    xaxis_title="Player",
    yaxis_title="Stats",
    barmode="group",
)
fig.show()
