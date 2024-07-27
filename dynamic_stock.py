import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.dates as mdates
from datetime import datetime
from typing import Optional
import pytz

#Create a dynamic stock that updates every 5 seconds with new stock information if market is open
class DynamicStock:
    
    def __init__(self, ticker: str, period: str, interval: str, testing: bool):
        self.ticker = ticker
        self.period = period
        self.interval = interval
        self.testing = testing
    
            
        date = datetime.now()
        newYorkTz = pytz.timezone("America/New_York") 
        timeInNewYork = datetime.now(newYorkTz)
        self.currentTimeInNewYork = timeInNewYork.strftime("%H:%M:%S")
        
        #drawing the figure    
        stock_data = self.fetch()
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot(stock_data['Close'], color='black', label='Closing Price')
        self.ax.set_title(f'{self.ticker} Stock Price')
        self.ax.set_xlabel('Date/Hour')
        self.ax.set_ylabel(f'{self.ticker} Price')
        self.ax.legend()
        
        #determining if the market is open or closed
        if int(self.currentTimeInNewYork[:2]) >= 16 or date.weekday() >= 5:
            stock_data = self.fetch()
            cur_stock_price = round(stock_data['Close'].iloc[-1],  4)
            print("Stock Market is Closed. Final Price Today was: $" + str(cur_stock_price))
            self.show()
        else:
            self.ani = FuncAnimation(self.fig, self.update, interval=5000, frames=100, repeat=False)
            self.show()
        

    #EFFECT: fetch stock data and return a pandas DataFrame
    def fetch(self) -> pd.DataFrame:
        stock_data = yf.download(self.ticker, period=self.period, interval=self.interval)
        return stock_data
    
    #EFFECT: update the graph with new stock information, being called from FuncAnimation
    def update(self, frame: Optional[int] = None) -> float: # pragma: no cove
        stock_data = self.fetch()
        
        if not stock_data.empty:
            cur_stock_price = round(stock_data['Close'].iloc[-1],  4)
            print("Current stock price: " + str(cur_stock_price))
            if not self.testing:
                self.line.set_data(stock_data.index, stock_data['Close'])
                self.ax.relim()
                self.ax.autoscale_view()
                self.fig.canvas.draw()
            return cur_stock_price
        
    #EFFECT: display graph
    def show(self) -> None:  # pragma: no cover
        plt.grid(True)
        plt.show()