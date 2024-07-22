import sys
import os
import pytest
import pandas as pd
import yfinance as yf
import numpy as np  # Import numpy for using assert_almost_equal


# Add the directory containing stock_analyzer.py to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import stock_analyzer as sa


def test_stock_data():
    data = sa.fetch_stock_history_data("NVDA", "2024-07-19", "2024-07-20")
    
    #expected
    expected_close = 117.93
    expected_open = 120.35
    expected_high = 121.60
    expected_low = 117.37

    #check if data is not empty
    assert not data.empty

    #unit tests
    np.testing.assert_almost_equal(data["Close"].iloc[-1], expected_close, decimal=2)
    np.testing.assert_almost_equal(data["Open"].iloc[-1], expected_open, decimal=2)
    np.testing.assert_almost_equal(data["High"].iloc[-1], expected_high, decimal=2)
    np.testing.assert_almost_equal(data["Low"].iloc[-1], expected_low, decimal=2)
    
def test_stock_data_return():
    assert isinstance(sa.fetch_stock_history_data("NVDA", "2024-07-19", "2024-07-20"), pd.DataFrame) 
    
def test_moving_average_exception():
    
    test_data = {'col1' : [1, 2, 3, 4, 5], 'col2' : [0, 0, 0, 0, 0]}
    pd_data = pd.DataFrame(data=test_data)
    with pytest.raises(Exception):
        sa.moving_average(pd_data, 5) == Exception("Invalid Stock: need \"Close\" column")
        
def test_moving_average():
    
    stock_data = yf.download("AAPL", start="2020-10-01", end="2020-10-11")
    
    #        [116.129997, 113.019997, 116.500000, 113.160004, 115.080002, 114.970001, 116.970001],

    new_moving_avg = stock_data["Close"].rolling(window=5).mean()
    
    expected = new_moving_avg.iloc[-1]
    
    output = sa.moving_average(stock_data, 5)
    
    fn_output = output.iloc[-1]
    
    assert isinstance(output, pd.Series)
    
    assert fn_output == expected
    
