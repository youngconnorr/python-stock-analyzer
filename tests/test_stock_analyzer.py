import sys
import os
import pytest
import pandas as pd
import yfinance as yf
import numpy as np  # Import numpy for using assert_almost_equal
import stock_analyzer as csOne

# Add parent directory to sys.path for module imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

cs = csOne.ChosenStock("NVDA", "2024-07-01", "2024-07-20")

def test_stock_data():
    data = cs.fetch_stock_history_data()
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
    assert isinstance(cs.fetch_stock_history_data(), pd.DataFrame) 
    
def test_moving_average_exception():
    test_data = {'col1': [1, 2, 3, 4, 5], 'col2': [0, 0, 0, 0, 0]}
    pd_data = pd.DataFrame(data=test_data)

    stockObjOne = csOne.ChosenStock("AAPL","2020-10-01", "2020-10-11")
    stockObjOne.stock_data = pd_data 
    
    with pytest.raises(ValueError, match="Invalid Stock: need \"Close\" column"):
        stockObjOne.moving_average(window=5)
        
def test_moving_average():
    stock_data = yf.download("NVDA", "2024-07-01", "2024-07-20")
    
    new_moving_avg = stock_data["Close"].rolling(window=10).mean()
    expected = new_moving_avg.iloc[-1]
    
    output = cs.moving_average(10)
    fn_output = output.iloc[-1]
    
    assert isinstance(output, pd.Series)
    assert (fn_output == expected) 
