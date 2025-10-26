"""
This is meant to test what is returned back using the AsyncFileReader function in src/async_reader.py
"""

import pytest
import pandas as pd
import os
import asyncio
from src.async_reader import AsyncFileReader

@pytest.mark.asyncio
async def test_async_read():
    """
    Simple test to check if async CSV reading returns a DataFrame.
    """
    # Temp CSV
    test_csv = "tests/test_data.csv"
    with open(test_csv, "w") as f:
        f.write("City,Elevation\n")
        f.write("Calgary,1045\n")
        f.write("Toronto,76\n")

    # async read CSV
    df = await AsyncFileReader.read_file_async(test_csv)

    # Check if it is a DataFrame and has rows
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0

    # Clean up
    os.remove(test_csv)
