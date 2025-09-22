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
    None

Globals:
    logger (logging.Logger): Configured logger instance for logging messages.

Author: Corbin Beus
Date: 09/20/2025
"""

from src import file_calculator, file_reader, display_results
from src.logger import setup_logger

# Global logger instance
logger = setup_logger()

if __name__ == '__main__':

    # File path to the CSV file
    logger.info("Looking for the CSV file...")
    try:
        # Read and store CSV file -> File path
        file_name = r"C:\Users\corbi\Downloads\CS3270\weather_data\canada_weather.csv" 

        # Use the static method in file_reader to read the CSV file -> Pandas DataFrame
        pd_data_frame = file_reader.FileReader.read_file(file_name)

        # Display the first 5 rows of the DataFrame using the display_results module -> DataFrame head
        head_of_dataframe = display_results.FileDisplay.display_csv_head(pd_data_frame)
        print(head_of_dataframe)
    except FileNotFoundError as fnf_error:
        logger.error(f"FileNotFoundError: {fnf_error}")
        raise
    except Exception as e:
        logger.critical(f"Unknown Error occurred while reading or display: {e}")
        raise
    logger.info("Successfully read the CSV file!")

    # Display the Mean, Median & Range of the Elevation column using the file_calculator & display_results modules
    logger.info("Calculating Elevation statistics...")
    try:
        elevation_stats = file_calculator.FileCalculator.elevation_statistics(pd_data_frame)
        display_results.FileDisplay.display_elevation_statistics(elevation_stats)
    except Exception as e:
        logger.critical(f"Unknown Error occurred while calculating or displaying statistics: {e}")
        raise
    logger.info("Successfully calculated and displayed Elevation statistics!")

