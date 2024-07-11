# read csv file and find minimum and maximum values in each column

import pandas as pd

def min_max_values_in_columns(csv_file):
    try:
        # Read CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file)
        
        # Find minimum and maximum values in each column
        min_max_values = df.agg(['min', 'max'])
        
        return min_max_values
    
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
        return None
    
    except pd.errors.EmptyDataError:
        print(f"Error: File '{csv_file}' is empty.")
        return None
    
    except pd.errors.ParserError:
        print(f"Error: Error parsing the file '{csv_file}'.")
        return None

csv_file = 'D:\course\Day_12_Practice_question\data.csv'

min_max_values = min_max_values_in_columns(csv_file)

if min_max_values is not None:
    print(min_max_values)
