# read csv file and generate a bar chart to represent data using matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read CSV file into a pandas DataFrame
filename = 'D:\course\Day_8_Practice_question\data.csv'  # Replace with your CSV file name
try:
    df = pd.read_csv(filename)
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    exit()

# Step 2: Prepare data for plotting
categories = df['Category']
values = df['Value']

# Step 3: Plotting
plt.figure(figsize=(10, 6))  # Adjust figure size as needed
plt.bar(categories, values, color='blue')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart of Categories vs Values')
plt.xticks(rotation=45)  # Rotate category labels if needed
plt.tight_layout()

plt.show()
