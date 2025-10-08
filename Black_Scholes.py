import scipy 
from scipy import stats
import numpy as numpy
from numpy import log, exp, sqrt

def call_option_price (S, E, T, rf, sigma):
    # calculate d1 and d2 
    d1=(log(S/E)+(rf+sigma*sigma/2)*T)/(sigma*sqrt(T)) 
    d2= d1 - sigma * sqrt(T) 
    print (d1, d2)
    # use the standart normal distribution ( N(x) ) 
    #to calculate the price of the call option
    return S * stats.norm.cdf(d1)-E*exp(-rf*T)*stats.norm.cdf(d2) 

def put_option_price (S, E, T, rf, sigma):
    # calculate d1 and d2 
    d1=(log(S/E)+(rf+sigma*sigma/2)*T)/(sigma*sqrt(T)) 
    d2= d1 - sigma * sqrt(T) 
    print (d1, d2)
    # use the standart normal distribution ( N(x) ) 
    #to calculate the price of the put option
    return -S * stats.norm.cdf(-d1)+E*exp(-rf*T)*stats.norm.cdf(-d2)

if __name__ == '__main__': 
    # price of the stock at T0
    S0 = 40
    # strike price 
    E = 100 
    # expiry 
    T = 1 
    # risk free rate
    rf = 0.05 
    # vol of the underlying stock  
    sigma = 0.2 

    print(call_option_price(S0, E, T, rf, sigma))
    print(put_option_price(S0, E, T, rf, sigma))
