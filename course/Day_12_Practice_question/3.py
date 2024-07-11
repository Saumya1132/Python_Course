# create pandas dataframe from dictionary and perform grouping and filtering operations

import pandas as pd

# Sample dictionary

data = {
    'Name': ['John', 'Jane', 'Mark', 'Sarah', 'Tom', 'Emily'],
    'Age': [25, 30, 35, 28, 32, 27],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'New York', 'Los Angeles']
}

# Create pandas dataframe

df = pd.DataFrame(data)

# Group by city and calculate average age

average_age_by_city = df.groupby('City')['Age'].mean()

# Filter dataframe to include only people aged between 25 and 30

filtered_df = df[(df['Age'] >= 25) & (df['Age'] <= 30)]

# Print the filtered dataframe

print(filtered_df)

# Print the average age by city

print(average_age_by_city)

