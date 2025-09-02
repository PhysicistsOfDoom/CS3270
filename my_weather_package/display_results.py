"""
This module provides a DATAFRAME interface for weather data analysis using Pandas.

Functions:
    display_statistics

"""
from .file_reader import read_file
from .file_calculator import elevation_statistics

def display_elevation_statistics(file_name: str) -> None:
    """
    This function is used to display ELEVATION stats gathered from the elevation_statics module.
    """
    stats = elevation_statistics(file_name)
    print("Elevation (meters) statistics:")
    print(f"Mean: {stats['mean']:.2f}")
    print(f"Median: {stats['median']:.2f}")
    print(f"Range: {stats['range']:.2f}")

def display_csv_dataframe(file_name: str) -> None:
    """
    This function displays CSV head from the provided weather data file.
    """
    df = read_file(file_name)
    print(df.head()) # Only print the head
    