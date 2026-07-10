
"""yfinance automatically returns the data as a pandas DataFrame,
so everything you do after (.head(), .describe(), .groupby(), .mean() etc.) is all standard pandas.
 That's exactly why we imported pandas at the top."""



import yfinance as yf
import pandas as pd 

oil=yf.download('CL=F', start='2020-01-01',end='2024-12-31')#CL=F is the ticker symbol for WTI Crude Oil Futures on Yahoo Finance.
#BZ=FBrent Crude Oil
print(oil.head())# first 5 rows (default)
print(oil.shape)#.shape tells you the dimensions of the DataFrame — how many rows and columns you have.


print(oil['Close'].describe())# Close is the close price of oil in that period and describe basically gives some stats abour it like mean and all
