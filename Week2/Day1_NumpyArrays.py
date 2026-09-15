##Install NumPy and create 1D and 2D arrays. Inspect shape, size, and number of dimensions.##

import numpy as np

# Create a 1D array
arr1 = np.array([10, 20, 30, 40, 50])

print("1D Array:", arr1)
print("Shape:", arr1.shape)
print("Size:", arr1.size)
print("Dimensions:", arr1.ndim)


# Create a 2D array
arr2 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\n2D Array:")
print(arr2)
print("Shape:", arr2.shape)
print("Size:", arr2.size)
print("Dimensions:", arr2.ndim)