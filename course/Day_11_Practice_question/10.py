# takes numpy arrays and returns a new array with the square values

import numpy as np

arr = np.random.randint(1,10,size= 5)

squared_arr = np.square(arr)

print("Original array:", arr)

print("Squared array:", squared_arr)