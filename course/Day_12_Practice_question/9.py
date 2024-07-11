# calculate sum of the specific column from csv file

import csv

def calculate_column_sum(csv_file, column_index):
    try:
        total_sum = 0
        with open(csv_file, mode='r') as file:
            csv_reader = csv.reader(file)
            
            next(csv_reader)  # Skip the header row
            
            for row in csv_reader:
                value = float(row[column_index])
                total_sum += value
                
            return total_sum
    
    except FileNotFoundError:
        print("File not found.")
        return None
    except ValueError:
        print("Error in data conversion.")
        return None
    
csv_file = "D:\course\Day_12_Practice_question\\temperatures.csv"

column_index = 1  # Change this to the desired column index

result = calculate_column_sum(csv_file, column_index)

if result is not None:
    print(f"Sum of the values in column {column_index + 1} is: {result}")
