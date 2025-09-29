"""
This module provides a DATAFRAME interface for weather data analysis using Pandas.

Functions:
    display_statistics

"""
from .logger import setup_logger
# Make a global logger instance
logger = setup_logger()

class FileDisplay:
    @staticmethod
    def display_elevation_statistics(stats: str) -> None:
        """
        This function is used to display ELEVATION stats gathered from the elevation_statics module.
        """
        print("Elevation (meters) statistics:")
        print(f"Mean: {stats['mean']:.2f}")
        print(f"Median: {stats['median']:.2f}")
        print(f"Range: {stats['range']:.2f}")
        
    @staticmethod
    def display_csv_head(results: dict):
        """
        This function displays CSV head from the provided weather data file.
        """
        yield results.head() # Only print the head
    