##Create or load a CSV file and inspect it using head, tail, info, and describe.##
import pandas as pd

data = {
    "Name": ["John", "Mike", "Sarah", "David", "Lisa"],
    "Age": [22, 25, 21, 24, 23],
    "Marks": [85, 90, 78, 92, 88],
    "Grade": ["B", "A", "C", "A", "B"]
}

df = pd.DataFrame(data)

df.to_csv("students.csv", index=False)

df = pd.read_csv("students.csv")

print("First 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nDataFrame information:")
print(df.info())

print("\nStatistical description:")
print(df.describe())