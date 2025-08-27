"""
main.py
-------
The Pandas Library in python, will read a weather CSV and then format it into a DataFrame.
"""

import csv
import pandas as pd

weather_data = [] # Data Structure for weather data.

def read_file(file_name):
    """
    Opens and reads CSV file

    Args:
        file_name(str): Path in your file system to CSV file

    Output:
        List of rows, in a column/row format.
    """
    with open(file_name, mode = 'r') as file:
        content = csv.reader(file)
        for lines in content:
            weather_data.append(lines)

def read_file_pandas(file_name):
    """
    Reads CSV file contents (Pandas module)

    Args:
        file_name (str): Path to the CSV in file system

    Output:
        A Dataframe containing the data 
    """
    content = pd.read_csv(file_name)
    return content


if __name__ == '__main__':
    file_name = r"C:\Users\corbi\Downloads\CS3270\weather\canada_weather.csv" # Adjust your user path 

    read_file(file_name)
    print("CSV Method ", len(weather_data))

    data_frame = read_file_pandas(file_name)
    print("Pandas Method ", len(data_frame))
    print(data_frame.head())