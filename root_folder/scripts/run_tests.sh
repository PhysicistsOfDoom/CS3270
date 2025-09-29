#!/bin/bash

cd "$(dirname "$(dirname "${BASH_SOURCE[0]}")")"

# Commands
python -m pytest tests/test_csv_analyze.py -v -s