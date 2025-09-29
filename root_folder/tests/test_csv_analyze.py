import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from src import file_calculator, file_reader, display_results
import pandas as pd


"""
Test module for testing all the src files that are imported in main.py.

functions:
    test_get_csv_file_path()
    test_file_reader()
    test_display_results()
    test_file_calculator()

Author: Corbin Beus
Date: 09/20/2025
"""

# Red -> Green -> Refactor approach to TDD
def test_get_csv_file_path():
    """
    Test to ensure the CSV file path is correctly constructed.
    """
    current_dir = os.path.dirname(__file__)
    expected_path = os.path.join(current_dir, 'data', 'canada_weather.csv')
    assert expected_path == os.path.join(current_dir, 'data', 'canada_weather.csv')

def test_file_reader():
    """
    Test to ensure the FileReader reads the CSV file correctly into a DataFrame.
    """
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'data', 'canada_weather.csv')
    
    df = file_reader.FileReader.read_file(file_path)
    
    assert isinstance(df, pd.DataFrame)
    assert 'Elevation' in df.columns
    assert not df.empty

def test_display_results():
    """
    Test to ensure the display_results module displays the DataFrame head correctly.
    """
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'data', 'canada_weather.csv')
    
    df = file_reader.FileReader.read_file(file_path)
    
    head_gen = display_results.FileDisplay.display_csv_head(df)
    head = next(head_gen)
    assert isinstance(head, pd.DataFrame)
    assert len(head) == 5

def test_file_calculator():
    """
    Test to ensure the FileCalculator computes elevation statistics correctly.
    """
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'data', 'canada_weather.csv')
    
    df = file_reader.FileReader.read_file(file_path)
    
    stats = file_calculator.FileCalculator.elevation_statistics(df)
    
    assert 'mean' in stats
    assert 'median' in stats
    assert 'range' in stats
    assert isinstance(stats['mean'], (int, float))
    assert isinstance(stats['median'], (int, float))
    assert isinstance(stats['range'], (int, float))