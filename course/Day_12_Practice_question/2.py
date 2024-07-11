# read csv file and perform basic malipulation operations

import pandas as pd

# Read CSV file and perform basic manipulation operations
filename = "D:\course\Day_12_Practice_question\employees.csv"
df = pd.read_csv(filename)

# Add a new column
df['Salary Increase'] = df['Salary'] * 0.10

# Update a value
df.loc[df['Name'] == 'John Doe', 'Salary'] = df.loc[df['Name'] == 'John Doe', 'Salary'] * 1.10

# Delete a column
df.drop('Salary Increase', axis=1, inplace=True)

# Save the modified dataframe to a new CSV file
df.to_csv('modified_employees.csv', index=False)

print(df)
print("Modified employees.csv file created successfully.")

# Read CSV file and perform basic aggregation operations
df = pd.read_csv(filename)

# Calculate the sum of salaries
total_salary = df['Salary'].sum()

# Calculate the average salary
average_salary = df['Salary'].mean()

# Calculate the maximum salary
max_salary = df['Salary'].max()

# Calculate the minimum salary
min_salary = df['Salary'].min()

print("Total Salary:", total_salary)
print("Average Salary:", average_salary)
print("Maximum Salary:", max_salary)
print("Minimum Salary:", min_salary)
