import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # 2. Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # 3. Create first line of best fit
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    plt.plot(x, slope*x + intercept, color='red')


    # 4. Create second line of best fit
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]
    x2 = df[df["Year"] >= 2000]["Year"]
    y2 = df[df["Year"] >= 2000]["CSIRO Adjusted Sea Level"]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(x2, y2)
    plt.plot(x2, slope2*x2 + intercept2, color='green')

    # 5. Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend(["All Data", "Fit (2000)"])

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()