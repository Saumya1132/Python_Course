# create array and reshape it to different shape\

import numpy as np

# Create a 1D array
arr_1d = np.array([1, 2, 3, 4, 5, 6])

# Reshape it to a 2D array (2 rows, 3 columns)
arr_2d = arr_1d.reshape(2, 3)
print("2D array:")
print(arr_2d)

# Reshape it to a 3D array (2 blocks, 1 row, 3 columns)
arr_3d = arr_1d.reshape(2, 1, 3)
print("3D array:")
print(arr_3d)
