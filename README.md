# Weather Data Analyzer

A Python package for reading, analyzing, and visualizing Canadian weather data.  
It calculates elevation statistics, displays results, and supports logging and testing.

---

## Phase Updates

### Phase 6:
Inside of src/visual_plot.py, data visualization and patterns have been used in order to show a useful visualization of the mean, median and range.
README updated.
main.py updated to call the src/visual_plot.py



### Phase 7:
Inside src/async_reader.py, I implemented the use of async programming to speed up the reading of the CSV using the asyncio package.
Also, inside tests/tests_async_reading.py is an implementation checking if the returned value is indeed a Dataframe, returned from the
async function.
README updated.
main.py updated with calling of async function
created tests_async_reading.py, async_reader.py 

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
```
---

## Running

### Option 1: Run main.py directly
```bash
python main.py
```
### Option 2: Use the shell script
```bash
./scripts/run_main.sh
```

---

## Tests
### Option 1: Run tests with pytest
```bash
pytest -v
```
### Option 2: Run tests with the helper script
```bash
./scripts/run_tests.sh
```
---

## Sample Output
```bash
Reading weather data from: data/canada_weather.csv
Data loaded successfully with 1000 rows and 8 columns

Elevation Statistics:
Mean: 485.7 m
Median: 320.0 m
Range: 2847.0 m
```