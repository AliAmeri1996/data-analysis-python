
"""yfinance automatically returns the data as a pandas DataFrame,
so everything you do after (.head(), .describe(), .groupby(), .mean() etc.) is all standard pandas.
 That's exactly why we imported pandas at the top."""


import matplotlib.pyplot as plt 
import yfinance as yf
import pandas as pd 

oil=yf.download('CL=F', start='2020-01-01',end='2024-12-31')#CL=F is the ticker symbol for WTI Crude Oil Futures on Yahoo Finance.in this line you can add interval='1wk' too
#BZ=FBrent Crude Oil
oil.columns = ['Close', 'High', 'Low', 'Open', 'Volume']

'''exploratory data analysis (EDA)'''
print(oil.columns)       # what columns exist
print(oil.shape)         # how many rows/columns
print(oil.head())        # first 5 rows
print(oil.dtypes)        # data types of each column
print(oil.describe())    # summary stats
print(oil.isnull().sum()) # any missing values?


# print(oil['Close'].describe())# Close is the close price of oil in that period and describe basically gives some stats abour it like mean and all


# #30-day rolling average ,average closing price over the last 30 days
# oil['MA30']=oil['Close'].rolling(30).mean()

# # Daily % change
# oil['Daily_Return']=oil['Close'].pct_change()*100 # ok so basically when we say oil['Daily_Return'] this way we're making a column called 
# #'Daily_Return'

# print(oil[['Close', 'MA30', 'Daily_Return']].tail(10))


# oil['Mean'] = oil['Close'].mean()# if we want to make a column we first have to make it like this


oil_price_over80=oil[oil['Close']>80]# so this is filtering the closes that are over 80 , the column is close
print(oil_price_over80)


# 3. Combining two conditions - price over 80 AND volume over 500k
oil_busy = oil[(oil['Close'] > 80) & (oil['Volume'] > 500000)]
print(oil_busy)
print(oil.dtypes)














# """now lets visulise the data with matplotlib"""

# oil['MA30']=oil['Close'].rolling(30).mean()
# oil['Close'].plot(label='Close Price', figsize=(12,6))
# oil['MA30'].plot(label='30 Day MA')
# plt.title('WTI Crude Oil Price 2020-2024')
# plt.xlabel('Date')
# plt.ylabel('Price (USD)')
# plt.legend()
# plt.show()