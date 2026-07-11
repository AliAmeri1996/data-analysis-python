import matplotlib.pyplot as plt
import yfinance as yf 
import pandas as pd 


gold=yf.download('GC=F', start='2020-01-01',end='2022-01-01')
print(gold.isnull().sum())
print("best day in oil market:", gold["Close"].max())
print("worst close day in the oil market:",gold['Close'].min())
