# Given a Pandas DataFrame, group the data by a specific column and calculate the mean of another column.


import pandas as pd

def group_and_calculate_mean(df, group_by_column, calculate_mean_column):

    grouped_df = df.groupby(group_by_column)[calculate_mean_column].mean().reset_index()
    return grouped_df

data = {
    'Department': ['Engineering', 'Marketing', 'Engineering', 'Finance', 'Marketing', 'Finance'],
    'Employee': ['John', 'Jane', 'Doe', 'Alice', 'Bob', 'Charlie'],
    'Salary': [60000, 75000, 65000, 90000, 72000, 88000]
}
df = pd.DataFrame(data)

grouped_df = group_and_calculate_mean(df, 'Department', 'Salary')

print(grouped_df)
