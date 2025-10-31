import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # 2. Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # 3. Create first line of best fit (1880–2050)
    linres1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_predict1 = pd.Series(range(1880, 2051))
    y_predict1 = linres1.intercept + linres1.slope * x_predict1
    plt.plot(x_predict1, y_predict1, 'r', label='Best Fit Line (1880–2050)')

    # 4. Create second line of best fit (2000–2050)
    df_recent = df[df["Year"] >= 2000]
    linres2 = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    x_predict2 = pd.Series(range(2000, 2051))
    y_predict2 = linres2.intercept + linres2.slope * x_predict2
    plt.plot(x_predict2, y_predict2, 'green', label='Best Fit Line (2000–2050)')

    # 5. Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # 6. Save and return the figure
    plt.savefig("sea_level_plot.png")
    return plt.gcf()
