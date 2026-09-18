##Use groupby to calculate counts and averages by category.##
import pandas as pd

data = {
    "Name": ["Vijay", "Rahul", "John", "David", "Mike", "Sam"],
    "Department": ["IT", "HR", "IT", "HR", "IT", "HR"],
    "Marks": [85, 90, 78, 92, 88, 75]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\nCount by Department:")
print(df.groupby("Department")["Name"].count())

print("\nAverage Marks by Department:")
print(df.groupby("Department")["Marks"].mean())