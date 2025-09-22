# Weather CSV to DataFrame
# Updates Phase 4:
1. main.py & all /src files have been edited with Logging & error handling.
2. display_csv_head has been edited to demonstrate generators using the "yield" command
3. File Paths have been adjusted to use the os module for exact file paths.
4. logger.py, /logs, app.log have been added to demonstrate custom logging.

## Overview
This Python Script will use **Pandas** to read a static CSV path and return a **DataFrame**

## Setup
1. Installed Python3.x (or above)
2. Installed Libraries using pip:
```bash
pip install -r requirements.txt
```

## Usage
1. Make sure the filepath is accessible within the directory. Preferred inside of the "weather_data" folder
2. Import my_weather_package from this repository
3. In main.py:          
```python
my_weather_package.display_csv_dataframe(file_name)
my_weather_package.display_elevation_statistics(file_name)
```

To Run:
```bash
python <path/to/main.py> 
```


