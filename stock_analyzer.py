import pandas as pd
import yfinance as yf
import matplotlib as plt

#add interval(1m) for very accurate stock prices
#if looking at history do 1d

#fetch the data from a specified stock
def fetch_stock_history_data(ticker: str, startDate: str, endDate: str) -> pd.DataFrame:
    stock_data = yf.download(ticker, start=startDate, end=endDate)
    return stock_data


