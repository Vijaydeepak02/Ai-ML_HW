##Calculate mean, median, and standard deviation with NumPy and compare with manual calculations where possible.##
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Array:")
print(arr)

mean_numpy = np.mean(arr)
median_numpy = np.median(arr)
std_numpy = np.std(arr)

mean_manual = sum(arr) / len(arr)

sorted_arr = np.sort(arr)

n = len(sorted_arr)

if n % 2 == 1:
    median_manual = sorted_arr[n // 2]
else:
    median_manual = (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2

variance_manual = sum((x - mean_manual) ** 2 for x in arr) / len(arr)
std_manual = variance_manual ** 0.5

print("\nMean:")
print("NumPy:", mean_numpy)
print("Manual:", mean_manual)

print("\nMedian:")
print("NumPy:", median_numpy)
print("Manual:", median_manual)

print("\nStandard Deviation:")
print("NumPy:", std_numpy)
print("Manual:", std_manual)