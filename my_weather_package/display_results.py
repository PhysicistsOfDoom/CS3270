"""
This module provides a DATAFRAME interface for weather data analysis using Pandas.

Functions:
    display_statistics

"""
from .file_reader import read_file
from .file_calculator import calculate_statistics

def display_statistics(file_name: str) -> None:
    """
    This function is used to display the statistics of the weather data.
    """
    stats = calculate_statistics(file_name)
    print(stats)

def display_csv_dataframe(file_name: str) -> None:
    """
    This function is used to display the weather data as a CSV.
    """
    df = read_file(file_name)
    print(df.to_csv(index=False))
    