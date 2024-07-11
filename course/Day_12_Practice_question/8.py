# using pandas data frame filter the rows to include only the rows were specific column meets condition

import pandas as pd

data = {'Name': ['John', 'Anna', 'Peter', 'Linda', 'Mike'],
        'Age': [25, 30, 28, 22, 32],
        'City': ['New York', 'Paris', 'London', 'Tokyo', 'Berlin']}

df = pd.DataFrame(data)

filtered_df = df[df['Age'] > 28]

print(filtered_df)


