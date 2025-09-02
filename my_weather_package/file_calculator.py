"""
This module is meant to provide the MEAN, MEDIAN and RANGE for a provided CSV dataset

Functions:
    calculate_statistics

"""

import file_reader

def calculate_statistics(file_name: str) -> dict:
    """
    Calculate basic statistics (mean, median, range) for a weather dataset.

    Args:
        file_name (str): Path to the CSV file.

    Returns:
        dict: A dictionary containing the mean, median, and range for each numeric column.
    """
    # Calls file_reader to get a pd.Dataframe of the provided CSV
    df = file_reader.read_file(file_name)

    # Calculate statistics given the DataFrame above
    stats = {
        "mean": df.mean(),
        "median": df.median(),
        "range": df.max() - df.min()
    }

    return stats
