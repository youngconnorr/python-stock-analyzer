import pytest
from datetime import datetime
import pandas as pd
import yfinance as yf
import numpy as np 
import stock_analyzer as sa
import dynamic_stock as ds


cs = sa.ChosenStock(["NVDA"], "2024-07-01", "2024-07-20", True)
ds = ds.DynamicStock("AAPL", "1d", "1m", True)


def test_stock_data():
    data = cs.fetch_stock_history_data("NVDA")
    # Expected values
    expected_close = 117.93
    expected_open = 120.35
    expected_high = 121.60
    expected_low = 117.37

    assert not data.empty

    np.testing.assert_almost_equal(data["Close"].iloc[-1], expected_close, decimal=2)
    np.testing.assert_almost_equal(data["Open"].iloc[-1], expected_open, decimal=2)
    np.testing.assert_almost_equal(data["High"].iloc[-1], expected_high, decimal=2)
    np.testing.assert_almost_equal(data["Low"].iloc[-1], expected_low, decimal=2)
    
def test_stock_data_return():
    assert isinstance(cs.fetch_stock_history_data("NVDA"), pd.DataFrame) 
    
def test_moving_average_exception():
    test_data = {'col1': [1, 2, 3, 4, 5], 'col2': [0, 0, 0, 0, 0]}
    pd_data = pd.DataFrame(data=test_data)

    stockObjOne = sa.ChosenStock(["AAPL"],"2020-10-01", "2020-10-11", False)
    
    with pytest.raises(ValueError, match="Invalid Stock: need \"Close\" column"):
        stockObjOne.moving_average(pd_data, 5)
        
def test_moving_average():
    stock_data = yf.download("NVDA", "2024-07-01", "2024-07-20")
    
    new_moving_avg = stock_data["Close"].rolling(window=10).mean()
    expected = new_moving_avg.iloc[-1]
    
    output = cs.moving_average(stock_data, 10)
    fn_output = output.iloc[-1]
    
    assert isinstance(output, pd.Series)
    assert (fn_output == expected)
    
def test_dyanmic_stock_fetch():
    
    stock_data = yf.download("AAPL", period="1d", interval="1m")
    pd_stock_data = pd.DataFrame(data=stock_data)
    expected = pd_stock_data['Close'].iloc[-1]
    
    fetched = ds.fetch()
    actual = fetched['Close'].iloc[-1]
    
    assert isinstance(fetched, pd.DataFrame)
    assert (actual == expected)
    
def test_dyanmic_stock_update():
    
    stock_data = yf.download("AAPL", period="1d", interval="1m")
    pd_stock_data = pd.DataFrame(data=stock_data)
    expected = round(pd_stock_data['Close'].iloc[-1], 4)
    
    actual = ds.update()
    
    assert isinstance (actual, float)
    
    assert (actual == expected)
    
    
    
    
    
    

    
