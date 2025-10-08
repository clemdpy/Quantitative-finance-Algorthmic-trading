import pandas as pd 
import numpy as np 
import yfinance as yf 
from scipy.stats import norm 

def download (stock, start, end): 
    ticker = yf.download(stock, start=start, end=end)['Close']
    data = pd.DataFrame(ticker) 
    return data

def log(data):
    data['Log return'] = np.log(data['C']/data['C'].shift(1))
    data = data[1:]
    return data

def var(position, c, mu, sigma):
    var = position*(mu - sigma * norm.ppf(1-c))
    print ('var is :',var)

stock = download('C',start='2020-01-01', end='2025-01-09')
stock = log(stock) 
stock 

s = 1e6 
c = 0.95
mu = stock['Log return'].mean() 
sigma = stock['Log return'].std() 

var (s, c, mu, sigma) 
