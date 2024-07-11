# generate a random numpy array and find min and max values

import numpy as np

arr = np.random.randint(1,20,size=15)
minimum = np.min(arr)
maximun = np.max(arr)

print(arr)
print(maximun)
print(minimum)