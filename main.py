import yfinance as yf
import stock_analyzer as stock_analyzer
if __name__ == "__main__":
    # apple = yf.Ticker("NVDA")
    # dividends = apple.dividends
    # splits = apple.splits
    data = stock_analyzer.fetch_stock_history_data("NVDA", "2024-07-19", "2024-07-20")
    print(data)