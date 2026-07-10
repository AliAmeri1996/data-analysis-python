import yfinance as yf
import pandas as pd 

oil=yf.download('CL=F', start='2020-01-01',end='2024-12-31')
print(oil.head())
print(oil.shape)
