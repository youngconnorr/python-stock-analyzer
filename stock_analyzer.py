import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from typing import Optional
#add interval(1m) for very accurate stock prices
#if looking at history do 1d

#fetch the data from a specified stock

class ChosenStock:
    
    def __init__(self, ticker: list, start_date: str, end_date: str, testing: bool):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        if not testing:
            self.run_static_program()
        
        
    def fetch_stock_history_data(self, ticker: str) -> pd.DataFrame:
        fetched_stock_data = yf.download(ticker, self.start_date, self.end_date)
        return fetched_stock_data
    

    def moving_average(self, stock_data: pd.DataFrame, window: int) -> pd.Series:
        if "Close" not in stock_data:
            raise ValueError("Invalid Stock: need \"Close\" column")
    
        moving_average = stock_data["Close"].rolling(window=window).mean()
        return moving_average
    
    def plot_stock_data(self, axis: int, stock_data: pd.DataFrame, ticker: str, moving_average: Optional[pd.Series] = None) -> None:
        axis.plot(stock_data['Close'], color='black', label='Closing Price')
    
        if moving_average is not None:
            axis.plot(moving_average, color='blue', label='Moving Average')
    
        axis.set_title(f'{ticker} Stock Price')
        axis.set_xlabel('Date')
        axis.set_ylabel(f'{ticker} Price')
        axis.grid(True)
        axis.legend()
        
    def run_static_program(self) -> None:
        
        num_tickers = len(self.ticker)
        fig, axis = plt.subplots(num_tickers, 1)
        
        if num_tickers == 1:
            axis = [axis]
        
        for index, t in enumerate(self.ticker):
            data = self.fetch_stock_history_data(t)
            moving_data = self.moving_average(data, 3)
            
            self.plot_stock_data(axis[index], data, t, moving_data)
        
        
        plt.tight_layout()
        plt.show()
        
        
        
        
        
            
        