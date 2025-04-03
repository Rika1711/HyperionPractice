# Compulsory Task 1

import numpy as np

# 1)
# Find out why the wrong_array does not create a two-dimensional array:
# wrong_format = np.array((1, 0, 0), (0, 1, 0), (0, 0, 1, dtype=float))
# Problem: incorrect syntax.
# Each row has to be in () - done correctly here.
# There should be [] around the array.
# The datatype has to be defined outside of the [].

# Write it the correct way.
correct_format = np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)], dtype=float)
print(correct_format)

# 2)
# What is the difference between a1 np.array([0, 0, 0])
# and a2 = np.array([[0, 0, 0]])?
a1 = np.array([0, 0, 0])
a2 = np.array([[0, 0, 0]])

print(a1.ndim, "\n", a1.shape)
print(a2.ndim, "\n", a2.shape)

# a1 is a 1-dimensional array. It contains 3 elements.
# a2 is a 2-dimensional array. It has one row with 3 elements.

# 3)
# Create the 3 by 4 by 4 array:
# arr = np.linspace(1, 48, 48).reshape(3, 4, 4)
# Index or slice it to obtain the desired output.

arr = np.linspace(1, 48, 48).reshape(3, 4, 4)
print(arr)

# 20.0
print(arr[1, 0, -1])

# [9.10.11.12.]
print(arr[0, 2])

# [[33.34.35.36.][37.38.39.40.][41.42.43.44.][45.46.47.48.]]
print(arr[2])

# [[36.35.][40.39.][44.43.][48.47.]]
print(arr[2, :, -1:-3:-1])

# [[13.9.5.1.][29.25.21.17.][45.41.37.33.]]
print(arr[:, -1:-5:-1, 0])

# [[1.4.][45.48.]]
arr1 = arr[[0, 2], [0, 3], :]
print(arr1[:, [0, 3]])

# [[25.26.27.28.], [29.30.31.32.], [33.34.35.36.], [37.38.39.40.]]

# Attempt 1:
arr2 = arr.flatten()
arr2 = arr2[24:40]
arr3 = arr2.reshape(4, 4)

print(arr3)
# This version prints a 2D array.
# The desired output looks like a list of arrays (separated by ',').
# Not a success.

# Attempt 2:
arr_to_list = arr3.tolist()
print(arr_to_list)
# This version creates a list.
# Problem: The elements are comma-separated.

# Attempt 3:
sub_arr = np.split(arr2, 4)
print(sub_arr)
# Using split array crates weird output.
# Here the output announces each array.
# The elements are again comma separated.
