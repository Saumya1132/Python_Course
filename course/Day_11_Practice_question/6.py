# using numpy find mean median and standard deviation of a data set

import numpy as np

def calculate_statistics(data_set):
    mean = np.mean(data_set)
    median = np.median(data_set)
    std_dev = np.std(data_set)
    return mean, median, std_dev

data_set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mean, median, std_dev = calculate_statistics(data_set)

print("mean", mean)
print("median", median)
print("std_dev", std_dev)

