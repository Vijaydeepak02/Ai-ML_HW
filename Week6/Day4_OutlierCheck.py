##Detect far-away points in a small numerical dataset using simple distance logic.##
import numpy as np

data = np.array([10, 12, 11, 13, 12, 100])

mean = np.mean(data)

distance = abs(data - mean)

for value, dist in zip(data, distance):
    if dist > 30:
        print("Outlier:", value)
    else:
        print("Normal:", value)