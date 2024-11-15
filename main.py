import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from scipy import stats

from monte_carlo import monte_carlo_simulation
from month_return import month_return
from bar_graph import plot_bar_graph
from gaussian import plot_gaussian
from shapiro import shapiro_test

ticker = "BTC-USD"
data = yf.download(ticker)


# Select parameters bellow : 
start_year = 2014
# choose the number of the month to analyze
month_to_analyze = 4
# choose the iteration for Monte-Carlo simulation
n_MC = 500
# choose the liquidation price, if exists
liq_price_MC = 0


plot_bar_graph(ticker, data, month_to_analyze, start_year)
plot_gaussian(ticker, data, month_to_analyze, start_year)
monte_carlo_simulation(ticker, data, month_to_analyze, start_year, n_MC, liq_price_MC)