"""
main.py
-------
In this Main module, we import all the src modules we need to read the CSV, Display and Calculate Elevation
statistics. We also set up logging to track the program's execution flow and handle any potential errors.

Modules:
    file_calculator
    file_reader
    display_results
    logger

Functions:
    get_csv_file_path()

Globals:
    logger (logging.Logger): Configured logger instance for logging messages.

Author: Corbin Beus
Date: 09/20/2025
"""

from src import file_calculator, file_reader, display_results, visual_plot
from src.logger import setup_logger
from src.async_reader import AsyncFileReader
from pyspark.sql import SparkSession
import os
import asyncio

# Global logger instance
logger = setup_logger()

# Function to get file path of the CSV file
def get_csv_file_path() -> str:
    """
    This function constructs the file path to the CSV file.
    Modify this function if the file path changes or if you want to make it dynamic.
    
    Returns:
        str: The file path to the CSV file.
    """
    # Example static path; modify as needed
    current_dir = os.path.dirname(__file__)
    csv_file_path = os.path.join(current_dir, 'data', 'canada_weather.csv')
    return csv_file_path

# Helper to attempt reading PySpark first and then fall back to pandas if it fails
def read_with_fallback(file_name):
    try:
        logger.info("Attempting to read CSV with PySpark...")
        spark = SparkSession.builder.appName("WeatherDataApp").getOrCreate()
        df_spark = spark.read.csv(file_name, header=True, inferSchema=True)
        logger.info("Successfully read CSV using PySpark!")

        df_pandas = df_spark.toPandas()
        return df_pandas

    except Exception as e:
        logger.warning(f"PySpark read failed: {e}")
        logger.info("Falling back to Pandas FileReader...")
        return file_reader.FileReader.read_file(file_name)

# Async call for CSV reading
async def fetch_csv():
    file_name = get_csv_file_path()
    logger.info("Reading CSV asynchronously...")
    df = await AsyncFileReader.read_file_async(file_name)
    return df

if __name__ == '__main__':

    # File path to the CSV file
    logger.info("Looking for the CSV file...")

    try:
        # Read and store CSV file -> File path
        file_name = get_csv_file_path()

        # Use the static method in file_reader to read the CSV file -> Pandas DataFrame
        pd_data_frame = file_reader.FileReader.read_file(file_name)

        # Display the first 5 rows
        head_of_dataframe = display_results.FileDisplay.display_csv_head(pd_data_frame)
        print(next(head_of_dataframe))

        # Calculate elevation stats
        elevation_stats = file_calculator.FileCalculator.elevation_statistics(pd_data_frame)
        display_results.FileDisplay.display_elevation_statistics(elevation_stats)

        # Display Results
        visual_plot.PlotResults.plot_elevation_statistics(elevation_stats)


    except FileNotFoundError as fnf_error:
        logger.error(f"FileNotFoundError: {fnf_error}")
        raise
    except Exception as e:
        logger.critical(f"Unknown Error occurred while reading or display: {e}")
        raise

    logger.info("Successfully read the CSV file!")
