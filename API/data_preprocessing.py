import pandas as pd

data = pd.read_csv("./AAPL.csv", header=[0, 1], index_col=0, parse_dates=True)

print("Column structure:")
print(data.columns)
print("\nData shape: ", data.shape)
print("\nFirst 10 rows:")
print(data.head())
