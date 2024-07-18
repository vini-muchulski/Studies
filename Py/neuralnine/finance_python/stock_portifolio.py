import datetime as dt
import matplotlib.pyplot as plt
#import pandas_datareader as web
import yfinance as yf

tickers = ["AMZN","MSFT","GOOG","APPL","AMD"]
amount = [10,10,10,10,10]
prices = []

total = []

for ticker in tickers:
    data = yf.download(ticker, start=dt.datetime(2018, 10, 27), end=dt.datetime.now())
    price = data['Adj Close'][0]
    prices.append(price)
    index = tickers.index(ticker)
    total.append(price * amount[index])



print(prices)
print(total)



print(prices)
print(total)

