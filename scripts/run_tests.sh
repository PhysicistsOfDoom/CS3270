#!/bin/bash
cd "$(dirname "$0")"/..

# Commands
python -m pytest tests/test_csv_analyze.py -v -s
pytest -v tests/tests_async_reading.py
