"""
This module provides a DATAFRAME interface for weather data analysis. Both with CSV and Pandas.

Functions:
    read_file

"""

import pandas as pd

class FileReader:
    @staticmethod
    def read_file(file_name: str) -> pd.DataFrame:
        """
        Reads a CSV file and returns its contents as a Pandas DataFrame.

        Args:
            file_name (str): Path to the CSV in file system

        Output:
            A Dataframe containing the data 
        """
        content = pd.read_csv(file_name)
        return content



