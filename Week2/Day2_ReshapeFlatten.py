##Use reshape and flatten on arrays and compare how the output changes.##
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

print("Original Array:")
print(arr)

reshaped = arr.reshape(2, 3)

print("\nReshaped Array:")
print(reshaped)

flattened = reshaped.flatten()

print("\nFlattened Array:")
print(flattened)