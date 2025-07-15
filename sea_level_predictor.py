import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]


    # Create scatter plot
    fig ,ax = plt.subplots(figsize=(10, 5))
    ax.scatter(x,y)


    # Create first line of best fit
    result = linregress(x, y)
    x_prediction = pd.Series(range(1880, 2051))
    y_prediction = result.slope * x_prediction + result.intercept
    ax.plot(x_prediction, y_prediction, "r", label="Fit: 1880–2050")


    # Create second line of best fit
    df_recent = df[df["Year"] >= 2000]
    res_recent = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    x_recent = pd.Series(range(2000, 2051))
    y_recent = res_recent.slope * x_recent + res_recent.intercept
    ax.plot(x_recent, y_recent, 'green', label='Fit: 2000–2050')

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()