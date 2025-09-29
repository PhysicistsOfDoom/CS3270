# Weather Data Analysis Package

A Python package for analyzing Canadian weather data with comprehensive statistical analysis and visualization capabilities.

## 📁 Project Structure

```
root_folder/
├── src/                          # Source code package
│   ├── __init__.py
│   ├── file_calculator.py        # Statistical calculations
│   ├── file_reader.py            # CSV file reading utilities
│   └── display_results.py        # Data display and formatting
├── tests/                        # Unit tests
│   └── test_csv_analyze.py       # Test suite for all modules
├── scripts/                      # Automation scripts
│   ├── run_main.sh               # Script to run main application
│   └── run_tests.sh              # Script to run test suite
├── weather_data/                 # Data directory
│   └── canada_weather.csv        # Sample Canadian weather data
├── logs/                         # Application logs
│   └── app.log                   # Runtime log file
├── main.py                       # Main application entry point
├── logger.py                     # Logging configuration
└── README.md                     # This file
```

## 🚀 Features

- **CSV File Reading**: Efficient reading and parsing of weather data files
- **Statistical Analysis**: Calculate mean, median, mode, range, and other descriptive statistics
- **Data Display**: Clean formatting and display of data and results
- **Elevation Statistics**: Specialized analysis of elevation data
- **Logging**: Comprehensive logging for debugging and monitoring
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 📋 Requirements

- Python 3.7+
- pandas
- pytest (for testing)

## 🔧 Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd root_folder
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

4. **Install dependencies:**
   ```bash
   pip install pandas pytest
   ```

## 🎯 Usage

### Running the Main Application

```bash
# Option 1: Direct execution from the root folder
python main.py

# Option 2: Using the automation script
./scripts/run_main.sh
```

### Running Tests

```bash
# Option 1: Direct pytest execution
python -m pytest tests/test_csv_analyze.py -v

# Option 2: Using the automation script
./scripts/run_tests.sh
```

### Using as a Package

```python
from src import file_reader, file_calculator, display_results

# Read CSV data
df = file_reader.FileReader.read_file('path/to/your/data.csv')

# Calculate statistics
stats = file_calculator.FileCalculator.elevation_statistics(df)

# Display results
display_results.FileDisplay.display_elevation_statistics(stats)
```

## 📊 Sample Output

```
Reading weather data from: weather_data/canada_weather.csv
Data loaded successfully with 1000 rows and 8 columns

Elevation Statistics:
Mean: 485.7 meters
Median: 320.0 meters
Mode: 156.0 meters
Range: 2847.0 meters
Standard Deviation: 512.3 meters
```

## 🧪 Testing

The project includes comprehensive unit tests covering:

- CSV file reading functionality
- Statistical calculation accuracy
- Data display formatting
- Error handling and edge cases

Run the test suite to verify functionality:
```bash
python -m pytest tests/ -v
```

## 📝 Logging

The application creates detailed logs in `logs/app.log` including:
- File operations
- Statistical calculations
- Error messages and stack traces
- Performance metrics

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 👤 Author

**Corbin Beus**
- Date: September 25, 2025
- Course: CS3270

## 🔍 Project Details

This project demonstrates:
- **Modular Design**: Clean separation of concerns across multiple modules
- **Test-Driven Development**: Comprehensive test coverage using pytest
- **Professional Logging**: Structured logging for production environments
- **Cross-Platform Compatibility**: Works across different operating systems
- **Data Analysis**: Statistical analysis of real-world weather data

## 📈 Future Enhancements

- [ ] Add data visualization with matplotlib
- [ ] Implement more advanced statistical analyses
- [ ] Add support for multiple file formats (JSON, Excel)
- [ ] Create web interface using Flask/FastAPI
- [ ] Add database integration for larger datasets