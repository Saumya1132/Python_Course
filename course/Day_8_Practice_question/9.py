# function reads json file and returns specific information from it.

import json

def read_json_file(filename, key):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data.get(key, None)  
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: '{filename}' is not a valid JSON file.")
        return None
    except KeyError:
        print(f"Error: Key '{key}' not found in '{filename}'.")
        return None

filename = 'D:\course\Day_8_Practice_question\data.json'  
key_to_extract = 'key_name'  

result = read_json_file(filename, key_to_extract)
if result is not None:
    print(f"The value associated with '{key_to_extract}' in '{filename}' is: {result}")
