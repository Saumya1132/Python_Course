# create pandas data frame and return the data in the ascending order

import pandas as pd

def create_dataframe_and_sort(data):
    df = pd.DataFrame(data)
    return df.sort_values(by=0)

data = [[5, 2, 8], [3, 1, 7], [8, 5, 3]]

sorted_df = create_dataframe_and_sort(data)

print (sorted_df)