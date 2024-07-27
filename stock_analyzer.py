import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from typing import Optional


#Creates a stock analysis of each ticker code given in a list of tickers
class ChosenStock:
    
    
    #EFFECT: initialize the chosen stock
    #note: check if object is a testing object or not with testing parameter
    def __init__(self, ticker: list, start_date: str, end_date: str, testing: bool):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        if not testing:
            self.run_static_program()
        
    #EFFECT: fetch data from yfinance API | return a pandas DataFrame
    def fetch_stock_history_data(self, ticker: str) -> pd.DataFrame:
        fetched_stock_data = yf.download(ticker, self.start_date, self.end_date)
        return fetched_stock_data
    
    #EFFECT: take in pandas DataFrame and use the Moving Average technique on the close section of the DataFrame | return a pandas Series (data as an array)
    def moving_average(self, stock_data: pd.DataFrame, window: int) -> pd.Series:
        if "Close" not in stock_data:
            raise ValueError("Invalid Stock: need \"Close\" column")
    
        moving_average = stock_data["Close"].rolling(window=window).mean()
        return moving_average
    
    #EFFECT: Create a plot taking in a DataFrame and optional moving average
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
        fig, axis = plt.subplots(num_tickers, 1, figsize=(10, 2 * num_tickers))
        
        if num_tickers == 1:
            axis = [axis]
        
        for index, t in enumerate(self.ticker):
            data = self.fetch_stock_history_data(t)
            moving_data = self.moving_average(data, 3)
            
            self.plot_stock_data(axis[index], data, t, moving_data)
        
        
        plt.tight_layout()
        plt.show()
        
        
        
        
        
            
        