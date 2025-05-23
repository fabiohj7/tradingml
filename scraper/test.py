import yfinance as yf

dat = yf.Ticker("AAPL")

print(dat.history(period='1mo'))
