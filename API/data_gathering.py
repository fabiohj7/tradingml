import pandas as pd
import yfinance as yf

START = "2020-01-01"
END = "2025-01-01"

tickers = ['AAPL', 'SKY', 'TNXP']

# Sky top loser tnxp top mover as of 05/28/2025
# data = yf.download(['AAPL', 'SKY', 'TNXP'], start=START, end=END)

# data.to_csv("stocks.csv")

for ticker in tickers:
    data = yf.download(ticker, start=START, end=END)
    data.to_csv(f"{ticker}.csv")

