import pandas as pd
import json

def read_json_and_extract_info(json_file, columns_to_extract):
    """
    Reads a JSON file into a Pandas DataFrame and extracts specific columns.

    Parameters:
    json_file (str): The path to the JSON file.
    columns_to_extract (list): List of columns to extract from the DataFrame.

    Returns:
    pd.DataFrame: DataFrame with the extracted columns.
    """
    try:
        # Open and read the JSON file
        with open(json_file, 'r') as file:
            data = json.load(file)
        
        # Check if data is a list (valid JSON for this context)
        if not isinstance(data, list):
            raise ValueError("JSON content is not a list.")
        
        # Convert the list of dictionaries to a DataFrame
        df = pd.DataFrame(data)
        
        # Check if all columns to extract are in the DataFrame
        for column in columns_to_extract:
            if column not in df.columns:
                raise KeyError(f"Column '{column}' not found in the DataFrame.")
        
        # Extract specific columns
        extracted_df = df[columns_to_extract]
        
        return extracted_df
    
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON file.")
    except ValueError as ve:
        print(ve)
    except KeyError as ke:
        print(ke)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Path to the JSON file
json_file = 'D:\course\Day_12_Practice_question\data.json'

# Columns to extract
columns_to_extract = ['name', 'department', 'salary']

# Read JSON file and extract information
extracted_df = read_json_and_extract_info(json_file, columns_to_extract)

if extracted_df is not None:
    print(extracted_df)
