import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd 

gold=yf.download('GC=F',start='2019-01-01',end='2025-01-01')
gold.columns=['Close',"High",'Low',"Open",'Volume']

#Explore the data first 

print("shape:", gold.shape)#tolist() just converts the columns index into a plain Python list so it prints cleanly like:
#['Close', 'High', 'Low', 'Open', 'Volume']
print("\nColumns:",gold.columns.tolist())#\n just adds a new line before "Columns:"
print("\nFirst 5 rows:")
print(gold.head())
print("\nData types:")
print(gold.dtypes)
print("\nSummary stats:")
print(gold.describe())
print("\nMissing values:")
print(gold.isnull().sum())