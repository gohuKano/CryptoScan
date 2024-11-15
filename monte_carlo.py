import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from scipy import stats

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

# Hypotheses pour l'utilisation de la methode de Monte-Carlo : 
# • les données sont distribuées selon une loi normale
def monte_carlo_simulation(ticker, data, month_index, start_year, num_of_simulation, liq_price):
    selected_month_data = data[(data.index.month == month_index) & (data.index.year < 2024) & (data.index.year >= start_year)]
    variation_by_day = 100 * (selected_month_data["Close"] - selected_month_data["Open"]) / selected_month_data["Open"]
    mean = np.mean(variation_by_day)
    stddev = np.std(variation_by_day)

    current_price = data["Close"].tail(1)[0]
    current_day = data["Close"].tail(1).index.day[0]

    # get how many days left of the month
    if month_index <= 7:
        if month_index % 2 == 1:
            # 31 jours
            days_left = 31 - current_day
        elif month_index % 2 == 0 and month_index != 2:
            # 30j
            days_left = 30 - current_day
        elif month_index == 2:
            # 28 jour
            days_left = 28 - current_day
    elif month_index >= 8:
        if month_index % 2 == 1:
            # 30j
            days_left = 30 - current_day
        elif month_index % 2 == 0:
            # 31j
            days_left = 31 - current_day

    MC_simulated_data = np.zeros((num_of_simulation, days_left))
    MC_simulated_data[:,0] = current_price

    # Monte Carlo simulation
    for i in range(1, days_left):
        MC_simulated_data[:, i] = MC_simulated_data[:, i - 1] * (1 + np.random.normal(mean, stddev, (num_of_simulation, ))/100)

    # Plot each row as a line
    for i in range(MC_simulated_data.shape[0]):
        plt.plot(MC_simulated_data[i, :], label=f"Simulation {i+1}", color='black', alpha=0.15)

    # Plot the mean line
    mean_line = np.mean(MC_simulated_data, axis=0)
    plt.plot(mean_line, color='blue', linestyle='-', linewidth=2, label='Mean')

    if liq_price != 0:
        # Plot the liquidation price
        plt.axhline(y=liq_price, color='red', linestyle='--', linewidth=2, label='Liq Price')
        plt.text(days_left, liq_price, "Liq Price", ha='right', va='center', color='red', fontsize=12)

    # Customize the plot
    plt.title(f"Monte Carlo Simulations for {ticker} on {months[month_index - 1]}s with Mean Line, n = {num_of_simulation}")
    plt.xlabel("Days")
    plt.ylabel("Price")

    # Add text annotations for mean, min, and max values
    mean_value = np.mean(MC_simulated_data[:, -1])
    min_value = np.min(MC_simulated_data)
    max_value = np.max(MC_simulated_data)

    plt.text(days_left, mean_value, f'Mean: {mean_value:.2f}', ha='right', va='center', color='blue', fontsize=12)
    plt.text(days_left, min_value, f'Min: {min_value:.2f}', ha='right', va='center', color='red', fontsize=12)
    plt.text(days_left, max_value, f'Max: {max_value:.2f}', ha='right', va='center', color='green', fontsize=12)

    plt.show()