Statistical Analysis of the Crypto Market
This project provides a statistical approach to analyzing the cryptocurrency market using Python. 
It incorporates tools such as Monte Carlo simulations, monthly return analysis, and statistical tests to gain insights into historical price data.

Features :
• Monthly Return Analysis: Visualize the performance of a specific month over multiple years.
• Gaussian Distribution Plot: Analyze the distribution of returns using a bell curve.
• Monte Carlo Simulation: Simulate potential price movements based on historical data.
• Shapiro-Wilk Test: Test the normality of monthly return distributions.

Parameters: You can customize the following parameters in main.py:
• ticker: The cryptocurrency ticker symbol (e.g., "BTC-USD").
• start_year: The year from which to start the analysis (e.g., 2014).
• month_to_analyze: The month to analyze (1 = January, ..., 12 = December).
• n_MC: Number of Monte Carlo simulation iterations.
• liq_price_MC: Liquidation price for Monte Carlo simulation (if applicable).

Requirements : 
To run the code, you’ll need the following Python libraries installed:
- pandas
- yfinance
- matplotlib
- numpy
- scipy
