# read csv file and process its data

import pandas as pd

filename= "D:\course\Day_8_Practice_question\employees.csv"
df= pd.read_csv(filename)
print(df.head())