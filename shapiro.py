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

def shapiro_test(data, month_index, start_year):
    values = month_return(data, month_index, start_year).flatten()
    res = stats.shapiro(values)

    if res.pvalue < 0.05:
        print(f"data from {months[month_index - 1]} month is not normaly distributed with p-value : {res.pvalue}")