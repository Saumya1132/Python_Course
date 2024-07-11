# using function that takes pandas data frame adds new calculated column to the dataframe 

import pandas as pd

def add_calculated_column(df, new_column_name, calculation_function):

    df[new_column_name] = calculation_function(df)
    return df

def calculate_sum(df):
    return df['Column1'] + df['Column2']

data = {
    'Column1': [10, 20, 30, 40],
    'Column2': [1, 2, 3, 4]
}
df = pd.DataFrame(data)

# Add a new calculated column 'Sum' to the DataFrame
df = add_calculated_column(df, 'Sum', calculate_sum)

print(df)


