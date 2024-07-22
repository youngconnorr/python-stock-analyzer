import sys
import os
import pytest
import numpy as np  # Import numpy for using assert_almost_equal


# Add the directory containing stock_analyzer.py to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import stock_analyzer as sa

def test_stock_data():
    data = sa.fetch_stock_history_data("NVDA", "2024-07-19", "2024-07-20")
    print(data)
    
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
