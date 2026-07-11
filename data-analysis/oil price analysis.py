
"""yfinance automatically returns the data as a pandas DataFrame,
so everything you do after (.head(), .describe(), .groupby(), .mean() etc.) is all standard pandas.
 That's exactly why we imported pandas at the top."""


import matplotlib.pyplot as plt 
import yfinance as yf
import pandas as pd 

oil=yf.download('CL=F', start='2020-01-01',end='2024-12-31')#CL=F is the ticker symbol for WTI Crude Oil Futures on Yahoo Finance.in this line you can add interval='1wk' too
#BZ=FBrent Crude Oil
oil.columns = ['Close', 'High', 'Low', 'Open', 'Volume']





''' 1-exploratory data analysis (EDA)= first thing to do to see what kind of data we have '''
print(oil.columns)       # what columns exist
print(oil.shape)         # how many rows/columns
print(oil.head())        # first 5 rows
print(oil.dtypes)        # data types of each column
print(oil.describe())    # summary stats
print(oil.isnull().sum()) # any missing values?

oil['Mean'] = oil['Close'].mean()# if we want to make a column we first have to make it like this





'''2- cleaning the data=Cleaning is about fixing problems in your data before you analyse it. The main things you'd check for:'''

print(oil.isnull().sum())# count missing values per column
oil.dropna()# remove rows with any missing value, no need to print 
oil.fillna(0)# fill missing with 0,no need to print 
oil.fillna(method='ffill')# fill with previous day's value (common in finance),no need to print 

#duplicate rows 
print(oil.duplicated().sum()) # count duplicatess
oil.drop_duplicates()


#Wrong data types
print(oil.dtypes) # check types
oil['Volume']=oil['volume'].astype(int) # convert to integer


#renaming messy columns names 
oil.rename(columns={'Close':'close_price'},inplace=True)\

#renaming columns you dont need
oil.drop(columns=['Volume'],inplace=True)





'''3- analysing the data now '''


#30-day rolling average ,average closing price over the last 30 days
oil['MA30']=oil['Close'].rolling(30).mean()

# Daily % change
oil['Daily_Return']=oil['Close'].pct_change()*100 # ok so basically when we say oil['Daily_Return'] this way we're making a column called 
#'Daily_Return'
print(oil[['Close', 'MA30', 'Daily_Return']].tail(10))

oil_price_over80=oil[oil['Close']>80]# so this is filtering the closes that are over 80 , the column is close
print(oil_price_over80)

# 3. Combining two conditions - # 4. How many days was oil above $80
# AND volume over 500k
oil_busy = oil[(oil['Close'] > 80) & (oil['Volume'] > 500000)]
print("Days above $80:",len(oil_busy))


# 2. Volatility per year (how much prices jumped around)
print(oil.groupby('Year')['Close'].std())


# 3. Best and worst trading days
oil['Daily_Return'] = oil['Close'].pct_change() * 100
print("best day in oil market:", oil["Close"].max())
print("worst close day in the oil market:",oil['Close'].min())
print("best day date:", oil['Daily_Return'].idmax())










# """now lets visulise the data with matplotlib"""

# oil['MA30']=oil['Close'].rolling(30).mean()
# oil['Close'].plot(label='Close Price', figsize=(12,6))
# oil['MA30'].plot(label='30 Day MA')
# plt.title('WTI Crude Oil Price 2020-2024')
# plt.xlabel('Date')
# plt.ylabel('Price (USD)')
# plt.legend()
# plt.show()