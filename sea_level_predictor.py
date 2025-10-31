import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # 2. Create figure and axes, then scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # 3. Create first line of best fit (1880–2050)
    linres1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_predict1 = pd.Series(range(1880, 2051))
    y_predict1 = linres1.intercept + linres1.slope * x_predict1
    ax.plot(x_predict1, y_predict1, 'r', label='Best Fit Line (1880–2050)')

    # 4. Create second line of best fit (2000–2050)
    df_recent = df[df["Year"] >= 2000]
    linres2 = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    x_predict2 = pd.Series(range(2000, 2051))
    y_predict2 = linres2.intercept + linres2.slope * x_predict2
    ax.plot(x_predict2, y_predict2, 'green', label='Best Fit Line (2000–2050)')

    # 5. Add labels, title, and ticks
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend()
    ax.set_xticks([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])

    # 6. Save the figure and return axes
    fig.savefig("sea_level_plot.png")
    return ax
