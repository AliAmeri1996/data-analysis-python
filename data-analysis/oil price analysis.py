
"""yfinance automatically returns the data as a pandas DataFrame,
so everything you do after (.head(), .describe(), .groupby(), .mean() etc.) is all standard pandas.
 That's exactly why we imported pandas at the top."""


import matplotlib.pyplot as plt 
import yfinance as yf
import pandas as pd 

oil=yf.download('CL=F', start='2020-01-01',end='2024-12-31')#CL=F is the ticker symbol for WTI Crude Oil Futures on Yahoo Finance.
#BZ=FBrent Crude Oil
print(oil.head())# first 5 rows (default)
print(oil.shape)#.shape tells you the dimensions of the DataFrame — how many rows and columns you have.


print(oil['Close'].describe())# Close is the close price of oil in that period and describe basically gives some stats abour it like mean and all


#30-day rolling average ,average closing price over the last 30 days
oil['MA30']=oil['Close'].rolling(30).mean()

# Daily % change
oil['Daily_Return']=oil['Close'].pct_change()*100 # ok so basically when we say oil'Daily_Return'] this way we're making a column called 
#'Daily_Return'

print(oil[['Close', 'MA30', 'Daily_Return']].tail(10))


oil['Mean'] = oil['Close'].mean()# if we want to make a column we first have to make it like this




"""now lets visulise the data with matplotlib"""

oil['MA30']=oil['Close'].rolling(30).mean()
oil['Close'].plot(label='Close Price', figsize=(12,6))
oil['MA30'].plot(label='30 Day MA')
plt.title('WTI Crude Oil Price 2020-2024')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()