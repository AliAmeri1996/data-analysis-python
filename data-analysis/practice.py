import matplotlib.pyplot as plt
import yfinance as yf 
import pandas as pd 


gold=yf.download('GC=F', start='2020-01-01',end='2022-01-01')
print(gold.columns)