# numpay array of random numbers and calculates its mean median and standard deviation

import numpy as np

# Generate a NumPy array of random numbers
random_array = np.random.rand(100)  # Array of 100 random numbers between 0 and 1

# Calculate the mean
mean = np.mean(random_array)

# Calculate the median
median = np.median(random_array)

# Calculate the standard deviation
std_deviation = np.std(random_array)

print("Random Array:", random_array)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_deviation)
