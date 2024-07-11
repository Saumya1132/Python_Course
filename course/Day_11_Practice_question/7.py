# takes list of numbers and returns the numpy array sorted in ascending order

import numpy as np

def sort_numpy_array(numbers):
    return np.sort(numbers)

numbers = [5, 3, 8, 1, 2, 7]

sorted_array = sort_numpy_array(numbers)

print(sorted_array)