# Weather Data Analyzer

A Python package for reading, analyzing, and visualizing Canadian weather data.  
It calculates elevation statistics, displays results, and supports logging and testing.

---

## Requirements

- Python 3.7+
- pandas  
- pytest (for testing)

---

## Installation 

```bash
# 1. Clone the repository
git clone <repository-url>
cd root_folder

# 2. Create and activate a virtual environment
python -m venv venv

# macOS/Linux
source venv/bin/activate

# 3. Install dependencies
pip install pandas pytest

## Running

# Option 1: Run main.py directly
python main.py

# Option 2: Use the shell script
./scripts/run_main.sh

## Tests
# Option 1: Run tests with pytest
pytest -v

# Option 2: Run tests with the helper script
./scripts/run_tests.sh

## Sample Output
Reading weather data from: data/canada_weather.csv
Data loaded successfully with 1000 rows and 8 columns

Elevation Statistics:
Mean: 485.7 m
Median: 320.0 m
Range: 2847.0 m
