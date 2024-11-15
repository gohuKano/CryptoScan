import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from month_return import month_return

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def plot_bar_graph(ticker, data, month_index, start_year):
    values = month_return(data, month_index, start_year).flatten()

    # Choose colors for bars
    colors = ['skyblue' if value < 0 else 'lightgreen' for value in values]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(np.arange(start_year, start_year + len(values)), values, color=colors,
                   edgecolor='black', linewidth=0.5)  # Add edge color for bars
    plt.title(f"{months[month_index - 1]} Variation for {ticker}", fontsize=16)  # Increase title font size
    plt.xlabel('Year', fontsize=14)  # Increase x-label font size
    plt.ylabel('%', fontsize=14)  # Increase y-label font size
    plt.xticks(rotation=45, fontsize=12)  # Rotate x-axis labels and increase font size

    # Add grid lines
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Add values above or below each bar
    for i, value in enumerate(values):
        plt.text(start_year + i, value, f'{value:.2f}%', ha='center',
                 va='bottom' if value >= 0 else 'top', fontsize=10, color='black')

    # Plot the mean line
    mean_value = np.mean(values)
    mean_line = plt.axhline(y=mean_value, color='orange', linestyle='--', linewidth=2, label='Mean')

    # Add text annotation for the mean line
    plt.text(start_year + len(values) - 0.5, mean_value, f'Mean: {mean_value:.2f}%', ha='right',
             va='center', color='orange', fontsize=12)

    # Draw horizontal line at 0
    plt.axhline(y=0, color='gray', linestyle='-', linewidth=1)

    # Add legend with shadow
    plt.legend(handles=[mean_line], loc='upper right', shadow=True, fontsize=12)

    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.show()

# Example usage:
# plot_bar_graph("AAPL", data, 4, 2010)
