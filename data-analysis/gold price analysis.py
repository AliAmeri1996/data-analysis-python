import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

gold=yf.download('GC=F',start='2019-01-01',end='2025-01-01')
gold.columns=['Close',"High",'Low',"Open",'Volume']

#1-Explore the data first

print("shape:", gold.shape)#Number of rows and columns
print("\nColumns:",gold.columns.tolist())#\n just adds a new line before "Columns:"tolist() just converts the columns index into a plain Python list so it prints cleanly like:
#['Close', 'High', 'Low', 'Open', 'Volume']
print("\nFirst 5 rows:")
print(gold.head())
print("\nData types:")
print(gold.dtypes)
print("\nSummary stats:")
print(gold.describe())
print("\nMissing values:")
print(gold.isnull().sum())



#2- cleaning the data file

print("\nnumber of missing values:")
print(gold.isnull().sum())

print("\nnumber of duplicates:")
print(gold.duplicated().sum())

gold=gold.dropna()#removes rows with missing values
gold = gold.drop_duplicates()


#3-Analysis 

print("\n Average price per year")
gold['Year']=gold.index.year #It creates a new column called Year by extracting just the year from the date index.
average_price_per_year=gold.groupby('Year')['Close'].mean()
print(average_price_per_year)
#groupby('Year') splits the data into groups — one group for each year (2020, 2021, 2022 etc). Then .mean() calculates the average Close price for each group separately.


print("\n best and worst day")
gold["Daily_Return"]=gold['Close'].pct_change()*100
best_day=gold["Daily_Return"].max()
worst_day=gold["Daily_Return"].min()
best_day_date = gold['Daily_Return'].idxmax()
worst_day_date = gold['Daily_Return'].idxmin()
print("\nbest day:",best_day,"\nworst day:",worst_day,"\n best day date:",best_day_date,"\n worst day date:",worst_day_date)

