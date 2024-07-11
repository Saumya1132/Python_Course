# using pandas perform operations like filtering and sorting

import pandas as pd

data = {
    'Name': ['John', 'Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 28, 32, 27],
    'City': ['New York', 'Los Angeles', 'Chicago', 'San Francisco', 'San Diego']
}

df = pd.DataFrame(data)

# Filter out people who are older than 30

filtered_df = df[df['Age'] > 30]

# Step 3: Sort data

# Sort the filtered data by age in descending order

sorted_df = filtered_df.sort_values(by='Age', ascending=False)

print(sorted_df)

# Group the data by city and calculate the average age

grouped_df = df.groupby('City')['Age'].mean()
print(grouped_df)

