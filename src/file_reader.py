"""
This module provides a DATAFRAME interface for weather data analysis.
This module now supports both PySpark & Pandas as of Phase 8

Class:
    FileReader
Functions:
    read_file

"""

import pandas as pd
from pyspark.sql import SparkSession
from .logger import setup_logger

# Global logger instance
logger = setup_logger()

class FileReader:
    @staticmethod
    def read_file(file_name: str, use_spark: bool = False):
        """
        Reads a CSV file and returns its contents as either a Pandas or PySpark DataFrame.

        Args:
            file_name (str): Path to the CSV in file system.
            use_spark (bool): If True, read the file using PySpark. Otherwise, use Pandas.

        Returns:
            DataFrame: Pandas or PySpark DataFrame depending on the 'use_spark' flag.
        """
        logger.info(f"Reading CSV file from {file_name} using {'PySpark' if use_spark else 'Pandas'}")

        try:
            if use_spark:
                # PySpark approach
                spark = SparkSession.builder \
                    .appName("WeatherDataAnalysis") \
                    .master("local[*]") \
                    .getOrCreate()

                df = spark.read.csv(file_name, header=True, inferSchema=True)
                logger.info("Successfully read CSV using PySpark!")
                return df, spark  

            else:
                # Pandas approach using Dataframes
                df = pd.read_csv(file_name)
                logger.info("Successfully read CSV using Pandas!")
                return df

        except FileNotFoundError as fnf_error:
            logger.error(f"FileNotFoundError: {fnf_error}")
            raise
        except Exception as e:
            logger.critical(f"Unknown error reading CSV: {e}")
            raise



