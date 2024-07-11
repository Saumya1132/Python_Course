# create 2D numpy array and find sum of elements in each row and column

import numpy as np

# Create a 2D numpy array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Calculate sum of elements in each row
row_sums = np.sum(arr, axis=1)

# Calculate sum of elements in each column
col_sums = np.sum(arr, axis=0)

print("Original 2D array:")
print(arr)
print("Row sums:", row_sums)
print("Column sums:", col_sums)
