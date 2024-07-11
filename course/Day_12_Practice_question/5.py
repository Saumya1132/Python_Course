# generate pandas series with dates and filter it to get dates in the specific range 

import pandas as pd

dates = pd.date_range('2022-01-01', '2022-12-31')

filtered_dates = dates[(dates.month >= 6) & (dates.month <= 8)]

print(filtered_dates)
