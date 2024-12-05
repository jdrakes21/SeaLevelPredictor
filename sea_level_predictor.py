import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], label='Sea Level Data', c='b', marker='o')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    x_values = range(1880, 2051)
    y_values = [slope * x + intercept for x in x_values]
    plt.plot(x_values, y_values, 'r', label='Best Fit Line (1880-2050)')

    # Create second line of best fit (since 2000)
    recent_data = data[data['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    x_values_recent = range(2000, 2051)
    y_values_recent = [slope_recent * x + intercept_recent for x in x_values_recent]
    plt.plot(x_values_recent, y_values_recent, 'g', label='Best Fit Line (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.legend()
    plt.savefig('sea_level_plot.png')
    return plt.gca()