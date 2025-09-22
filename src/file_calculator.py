"""
This module extracts the meters column from the CSV file and calculates MEAN, MEDIAN & RANGE.

Functions:
    extract_elevation_meters
    elevation_statistics

"""

import pandas as pd
import re

class FileCalculator:
    @staticmethod
    def extract_elevation_meters(elevation_str):
        """
        Extract the meter value from an elevation string like '1,084m (3,556ft)'.
        Returns float value or NaN if not found.
        """
        if isinstance(elevation_str, str):
            match = re.search(r'([\d,]+)m', elevation_str)
            if match:
                return float(match.group(1).replace(',', ''))
        return float('nan')

    @staticmethod
    def elevation_statistics(df: pd.DataFrame) -> dict:
        """
        This function will use the meter values to calculate MEAN, MEDIAN & RANGE
        """
        elevation_meters = df['Elevation'].apply(FileCalculator.extract_elevation_meters)
        stats = {
            "mean": elevation_meters.mean(),
            "median": elevation_meters.median(),
            "range": elevation_meters.max() - elevation_meters.min()
        }
        return stats
