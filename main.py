"""
main.py
-------
The Pandas Library in python, will use my_weather_package to read a given CSV. 
Then Display it as a DATAFRAME & Provide basic statistics.
"""

from my_weather_package import file_calculator, file_reader, display_results

if __name__ == '__main__':
    file_name = r"C:\Users\corbi\Downloads\CS3270\weather_data\canada_weather.csv" 

    # Read the file and get the DataFrame
    pd_data_frame = file_reader.read_file(file_name)
    
    # Display the DataFrame
    head_of_dataframe = display_results.display_csv_dataframe(pd_data_frame)
    print(head_of_dataframe)

    # Display the Mean, Median & Range of the Elevation column
    elevation_stats = file_calculator.elevation_statistics(pd_data_frame)
    display_results.display_elevation_statistics(elevation_stats)

