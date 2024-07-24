import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from typing import Optional
#add interval(1m) for very accurate stock prices
#if looking at history do 1d

#fetch the data from a specified stock

class ChosenStock:
    
    def __init__(self, ticker: list, start_date: str, end_date: str):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.run_program()
        
        
    def fetch_stock_history_data(self, ticker: str) -> pd.DataFrame:
        fetched_stock_data = yf.download(ticker, self.start_date, self.end_date)
        return fetched_stock_data
    

    def moving_average(self, stock_data: pd.DataFrame, window: int) -> pd.Series:
        if "Close" not in stock_data:
            raise ValueError("Invalid Stock: need \"Close\" column")
    
        moving_average = stock_data["Close"].rolling(window=window).mean()
        return moving_average
    
    def plot_stock_data(self, stock_data: pd.DataFrame, ticker: str, moving_average: Optional[pd.Series] = None) -> None:
        plt.plot(stock_data['Close'], color='black', label='Closing Price')
    
        if moving_average is not None:
            plt.plot(moving_average, color='black', label='Closing Price')
    
        plt.title(f'{ticker} Stock Price')
        plt.xlabel('Date')
        plt.ylabel(f'{ticker} Price')
        plt.legend()
        plt.show()
        
    def run_program(self) -> None:
        
        data_list = []
        moving_data_list = []
        
        for t in self.ticker:
            data = self.fetch_stock_history_data(t)
            data_list.append(data)
            
            moving_data = self.moving_average(data, 3)
            moving_data_list.append(moving_data)
            
            self.plot_stock_data(data, t, moving_data)
        
        
        
            
        