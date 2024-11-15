import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from scipy import stats

def month_return(data, month_index, start_year):
    """
    Calculate the percentage variation for a specific month across historical years.

    Parameters:
    - data (pd.DataFrame): Financial data from yfinance.
    - month_index (int): Index of the month to study (1 for January, 2 for February, and so on).

    Returns:
    - percentage_by_month (pd.DataFrame): Array of the percentage variation for each month across historical years.
    """

    # Select the month to study
    selected_month_data = data[(data.index.month == month_index) & (data.index.year < 2024) & (data.index.year > start_year)]

    if month_index <= 7:
        if month_index % 2 == 1:
            # Get the closing prices on the first and last day of the month
            start_month = pd.DataFrame(selected_month_data[selected_month_data.index.day == 1]["Open"]).values
            end_month = pd.DataFrame(selected_month_data[selected_month_data.index.day == 31]["Close"]).values
        elif month_index % 2 == 0 and month_index != 2:
            # Get the closing prices on the first and last day of the month
            start_month = pd.DataFrame(selected_month_data[selected_month_data.index.day == 1]["Open"]).values
            end_month = pd.DataFrame(selected_month_data[selected_month_data.index.day == 30]["Close"]).values
        elif month_index == 2:
            # Get the closing prices on the first and last day of the month
            start_month = pd.DataFrame(selected_month_data[selected_month_data.index.day == 1]["Open"]).values
            end_month = pd.DataFrame(selected_month_data[selected_month_data.index.day == 28]["Close"]).values
        
    elif month_index >= 8:
        if month_index % 2 == 1:
            # Get the closing prices on the first and last day of the month
            start_month = pd.DataFrame(selected_month_data[selected_month_data.index.day == 1]["Open"]).values
            end_month = pd.DataFrame(selected_month_data[selected_month_data.index.day == 30]["Close"]).values
        elif month_index % 2 == 0:
            # Get the closing prices on the first and last day of the month
            start_month = pd.DataFrame(selected_month_data[selected_month_data.index.day == 1]["Open"]).values
            end_month = pd.DataFrame(selected_month_data[selected_month_data.index.day == 31]["Close"]).values


    # print(f"{start_month} \n\n {end_month} ")
    # print(f"{start_month.shape} \n {end_month.shape} ")
    percentage_by_month = (100 * (end_month - start_month)/ start_month)
    return percentage_by_month