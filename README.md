# Pet Preference Counter 

A lightweight Python script that parses a CSV file to count pet preferences (cats, dogs, and birds). Built to practice reading files with `csv.DictReader` and aggregating categorical data with dictionaries using standard Python.

##How It Works
1. Opens `data.csv` and parses each row as a dictionary.
2. Iterates through the records to count occurrences of each animal type.
3. Prints the total counts to the terminal.

## Files
- `main.py` — The Python script that handles the file reading and counting logic.
- `data.csv` — Dataset containing respondent names and their preferred pets.

## Running the Script
No extra packages needed just run it with standard Python 3:

```bash
python main.py
