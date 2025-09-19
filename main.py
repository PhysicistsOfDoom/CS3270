"""
main.py
-------
The Pandas Library in python, will use my_weather_package to read a given CSV. 
Then Display it as a DATAFRAME & Provide basic statistics.
"""

from my_weather_package import file_calculator, file_reader, display_results

if __name__ == '__main__':
    file_name = r"C:\Users\corbi\Downloads\CS3270\weather_data\canada_weather.csv" 

    # No objects. Just static methods. So call the methods directly.
    pd_data_frame = file_reader.FileReader.read_file(file_name)
    
    # Use the static method in display_results to display the head of the dataframe
    head_of_dataframe = display_results.FileDisplay.display_csv_head(pd_data_frame)
    print(head_of_dataframe)

    # Display the Mean, Median & Range of the Elevation column using the file_calculator & display_results modules
    elevation_stats = file_calculator.FileCalculator.elevation_statistics(pd_data_frame)
    display_results.FileDisplay.display_elevation_statistics(elevation_stats)

