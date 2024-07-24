import yfinance as yf
import stock_analyzer as cs

if __name__ == "__main__":
    tickers = ["AAPL", "AMZN", "TSLA"]
    
    stock = cs.ChosenStock(tickers,"2012-10-01", "2020-10-11")
    