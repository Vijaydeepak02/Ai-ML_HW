## Conduct a coding test on arrays, DataFrames, filtering, and basic statistics. ##
import numpy as np
import pandas as pd

marks = np.array([85, 72, 30, 25, 95])

print("Array:", marks)

data = {
    "Name": ["Vijay", "Rahul", "sai", "Deepak", "satya"],
    "Marks": marks
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

print("\nStudents with marks above 35:")
print(df[df["Marks"] > 35])

print("\nAverage Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())