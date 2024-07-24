import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime
import pytz


class DynamicStock:
    
    def __init__(self, ticker: str, period: str, interval: str):
        self.ticker = ticker
        self.period = period
        self.interval = interval
        
        newYorkTz = pytz.timezone("America/New_York") 
        timeInNewYork = datetime.now(newYorkTz)
        self.currentTimeInNewYork = timeInNewYork.strftime("%H:%M:%S")
        
        if int(self.currentTimeInNewYork[:2]) > 16:
            stock_data = self.fetch()
            cur_stock_price = round(stock_data['Close'].iloc[-1],  4)
            print("Stock Market is Closed. Final Price Today was: " + str(cur_stock_price))

        else:
        
            self.fig, self.ax = plt.subplots()
            self.line, = self.ax.plot([], [], color='black', label='Closing Price')
            self.ax.set_title(f'{self.ticker} Stock Price')
            self.ax.set_xlabel('Date')
            self.ax.set_ylabel(f'{self.ticker} Price')
            self.ax.legend()
            
            self.ani = FuncAnimation(self.fig, self.update, interval=10000, frames=100, repeat=False)
        

    
    def fetch(self) -> pd.DataFrame:
        # Fetch stock data
        stock_data = yf.download(self.ticker, period=self.period, interval=self.interval)
        return stock_data
    
    def update(self, frame) -> None:
        # Update stock data
        stock_data = self.fetch()
        
        if not stock_data.empty:
            cur_stock_price = round(stock_data['Close'].iloc[-1],  4)
            self.line.set_data(stock_data.index, stock_data['Close'])
            self.ax.relim()
            self.ax.autoscale_view()
            self.fig.canvas.draw()
        
        print("Current stock price: " + str(cur_stock_price))
        
    
    def show(self) -> None:
        plt.show()