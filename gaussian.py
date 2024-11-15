import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from scipy import stats

from month_return import month_return

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def plot_gaussian(ticker, data, month_index, start_year):
    values = month_return(data, month_index, start_year).flatten()

    mean = np.mean(values)
    std_dev = np.std(values)

    # Generate a range of x values for the Gaussian plot
    x_range = np.linspace(mean - 4 * std_dev, mean + 4 * std_dev, 2000)

    # Calculate the corresponding y values for the Gaussian plot
    y_values = norm.pdf(x_range, mean, std_dev)

    # Plot the Gaussian distribution
    plt.plot(x_range, y_values, label='Gaussian Distribution', color='blue')

    # Plot vertical lines for mean, 1 sigma, and 2 sigmas
    plt.axvline(0, color='black', linestyle='-', label='Mean')
    plt.axvline(mean, color='gray', linestyle='-', label='Mean')
    plt.axvline(mean + std_dev, color='green', linestyle='--', label='Mean + 1 Sigma')
    plt.axvline(mean - std_dev, color='green', linestyle='--', label='Mean - 1 Sigma')
    plt.axvline(mean + 2 * std_dev, color='orange', linestyle='--', label='Mean + 2 Sigma')
    plt.axvline(mean - 2 * std_dev, color='orange', linestyle='--', label='Mean - 2 Sigma')
    plt.axvline(mean + 3 * std_dev, color='red', linestyle='--', label='Mean + 3 Sigma')
    plt.axvline(mean - 3 * std_dev, color='red', linestyle='--', label='Mean - 3 Sigma')

    # Annotate values for mean and sigmaes
    plt.text(mean, max(y_values), f'Mean: {mean:.2f}%', color='red', ha='center', va='bottom')
    plt.text(mean + std_dev, max(y_values), f'1 Sigma: {mean + std_dev:.2f}%', color='green', ha='center', va='bottom')
    plt.text(mean - std_dev, max(y_values), f'1 Sigma: {mean - std_dev:.2f}%', color='green', ha='center', va='bottom')
    plt.text(mean + 2 * std_dev, max(y_values), f'2 Sigma: {mean + 2 * std_dev:.2f}%', color='orange', ha='center', va='bottom')
    plt.text(mean - 2 * std_dev, max(y_values), f'2 Sigma: {mean - 2 * std_dev:.2f}%', color='orange', ha='center', va='bottom')
    plt.text(mean + 3 * std_dev, max(y_values), f'3 Sigma: {mean + 3 * std_dev:.2f}%', color='red', ha='center', va='bottom')
    plt.text(mean - 3 * std_dev, max(y_values), f'3 Sigma: {mean - 3 * std_dev:.2f}%', color='red', ha='center', va='bottom')

    plt.title(f"Gaussian Distribution for month {months[month_index - 1]} for {ticker}")
    plt.xlabel('% Variation')
    plt.ylabel('Probability Density')
    # plt.legend()
    plt.show()