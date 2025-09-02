"""
main.py
-------
The Pandas Library in python, will use my_weather_package to read a given CSV. 
Then Display it as a DATAFRAME & Provide basic statistics.
"""

import my_weather_package

if __name__ == '__main__':
    file_name = r"C:\Users\corbi\Downloads\CS3270\weather_data\canada_weather.csv" 

my_weather_package.display_csv_dataframe(file_name)
my_weather_package.display_elevation_statistics(file_name)
