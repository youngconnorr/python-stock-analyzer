import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.dates as mdates
from datetime import datetime
import pytz


class DynamicStock:
    
    def __init__(self, ticker: str, period: str, interval: str, testing: bool):
        self.ticker = ticker
        self.period = period
        self.interval = interval
    
            
        
        newYorkTz = pytz.timezone("America/New_York") 
        timeInNewYork = datetime.now(newYorkTz)
        self.currentTimeInNewYork = timeInNewYork.strftime("%H:%M:%S")
        
        if int(self.currentTimeInNewYork[:2]) >= 16:
            stock_data = self.fetch()
            cur_stock_price = round(stock_data['Close'].iloc[-1],  4)
            print("Stock Market is Closed. Final Price Today was: " + str(cur_stock_price))
        
        if testing:
            print("hello world")
        else:    
            stock_data = self.fetch()
            self.fig, self.ax = plt.subplots()
            self.line, = self.ax.plot(stock_data['Close'], color='black', label='Closing Price')
            self.ax.set_title(f'{self.ticker} Stock Price')
            self.ax.set_xlabel('Date/Hour')
            self.ax.set_ylabel(f'{self.ticker} Price')
            # self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
            # self.ax.xaxis.set_major_locator(mdates.HourLocator(tz='America/New_York'))
            self.ax.legend()
            self.show()
            
            if int(self.currentTimeInNewYork[:2]) < 16:
                self.ani = FuncAnimation(self.fig, self.update, interval=5000, frames=100, repeat=False)
        

    
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
            self.ax.text(0.1, 60, "HESHESIHDI", fontsize = 22)
            self.ax.relim()
            self.ax.autoscale_view()
            self.fig.canvas.draw()
        
        print("Current stock price: " + str(cur_stock_price))
        
    
    def show(self) -> None:
        plt.grid(True)
        plt.show()