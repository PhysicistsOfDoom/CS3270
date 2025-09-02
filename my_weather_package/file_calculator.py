"""
This module extracts the meters column from the CSV file and calculates MEAN, MEDIAN & RANGE.

Functions:
    extract_elevation_meters
    elevation_statistics

"""

from .file_reader import read_file
import re

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

def elevation_statistics(file_name: str) -> dict:
    """
    This function will use the meter values to calculate MEAN, MEDIAN & RANGE
    """
    df = read_file(file_name)
    elevation_meters = df['Elevation'].apply(extract_elevation_meters)
    stats = {
        "mean": elevation_meters.mean(),
        "median": elevation_meters.median(),
        "range": elevation_meters.max() - elevation_meters.min()
    }
    return stats
