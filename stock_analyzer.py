import pandas as pd
import yfinance as yf
import matplotlib as plt

#add interval(1m) for very accurate stock prices
#if looking at history do 1d

#fetch the data from a specified stock

class ChosenStock:
    
    ticker = ""
    start_date = ""
    end_date = ""
    stock_data = None
    
    def __init__(self, ticker: str, start_date: str, end_date: str):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.stock_data = self.fetch_stock_history_data()
        
        
        
    def fetch_stock_history_data(self) -> pd.DataFrame:
        fetched_stock_data = yf.download(self.ticker, self.start_date, self.end_date)
        print(fetched_stock_data)
        return fetched_stock_data
    

    def moving_average(self, window: int) -> pd.Series:
        if "Close" not in self.stock_data:
            raise ValueError("Invalid Stock: need \"Close\" column")
    
        moving_average = self.stock_data["Close"].rolling(window=window).mean()
        print(moving_average)
        return moving_average







