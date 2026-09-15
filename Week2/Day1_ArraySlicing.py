##Practice accessing elements, rows, and columns using indexing and slicing on arrays.##
import numpy as np


arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Print the complete array
print("2D Array:")
print(arr)


print("\nIndividual Elements:") #Accessing individual elements

print("First element:", arr[0, 0])
print("Element at row 1, column 1:", arr[1, 1])
print("Last element:", arr[2, 2])


print("\nRows:") #Acessing rows

print("First row:", arr[0])
print("Second row:", arr[1])
print("Third row:", arr[2])


print("\nColumns:")  #Accessing columns

print("First column:", arr[:, 0])
print("Second column:", arr[:, 1])
print("Third column:", arr[:, 2])


print("\nSlicing Rows:") #slicing rows

print("First two rows:")
print(arr[0:2])


print("\nSlicing Columns:") #slicing columns

print("First two columns:")
print(arr[:, 0:2])

print("\nSlicing Rows and Columns:") #slicing rows and columns

print("First two rows and first two columns:")
print(arr[0:2, 0:2])

print("First two rows and last two columns:")
print(arr[0:2, 1:3])