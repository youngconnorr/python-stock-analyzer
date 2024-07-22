import yfinance as yf
import stock_analyzer as cs

if __name__ == "__main__":
    # apple = yf.Ticker("NVDA")
    # dividends = apple.dividends
    # splits = apple.splits
    # data = stock_analyzer.fetch_stock_history_data("NVDA", "2020-05-10", "2024-07-20")
    # moving_av = stock_analyzer.moving_average(data, 5)
    # print(moving_av)
    AAPL = cs.ChosenStock("AAPL","2020-10-01", "2020-10-11")
    
    moving_avg = AAPL.moving_average(window=5)

    print(moving_avg)
