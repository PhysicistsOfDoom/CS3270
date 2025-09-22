"""
This module provides a DATAFRAME interface for weather data analysis. Both with CSV and Pandas.

Class:
    FileReader
Functions:
    read_file

"""

import pandas as pd
from .logger import setup_logger
# Make a global logger instance
logger = setup_logger()

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
        logger.info(f"Reading CSV file from {file_name}")
        try:
            content = pd.read_csv(file_name)
        except FileNotFoundError as fnf_error:
            logger.error(f"FileNotFoundError: {fnf_error}")
            raise
        logger.info("Successfully read the CSV file!")
        return content



