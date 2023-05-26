# NBA MVP Performance Based Predictive Model

This is a Python program that analyzes the performance of NBA players and predicts the top MVP candidates based purely on their stats and performances. It uses the pandas library to scrape NBA season stat leaders data from basketball-reference.com, and then performs data cleaning and exploratory data analysis using Plotly to create interactive charts.

## How it works

1. **Data Acquisition:** The program collects NBA season stat leaders data from basketball-reference.com using pandas to read the HTML table into a DataFrame.

2. **Data Cleaning:** The program cleans the data by removing unnecessary columns, renaming columns, removing duplicates, and converting relevant columns to numeric data type.

3. **Exploratory Data Analysis:** The program performs exploratory data analysis using Plotly to create interactive charts that display top 5 MVP candidates based on their points, rebounds, assists, games played, and minutes played.

4. **MVP Performance Prediction:** The program predicts the top MVP candidates based on their stats using a scoring system that adds up their points, rebounds, and assists, minutes & games played.

## How to use it

To use this program, you can follow these steps:

1. Clone the repository to your local machine.

2. Open the terminal and navigate to the cloned repository.

3. Install the required Python libraries using pip: Pandas and Matplotlib.

4. Run the main script "main.py" to perform the data analysis and generate the visualizations.

5. To customize the analysis, modify the code in the "main.py" script.

That's it! You can now use this program to analyze the performance of NBA players and predict the top MVP candidates based on their stats.
