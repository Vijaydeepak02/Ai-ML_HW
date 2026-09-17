##Select single and multiple columns and filter rows with conditions.##
import pandas as pd

data = {
    "Name": ["John", "Mike", "Sarah", "David", "Lisa"],
    "Age": [22, 25, 21, 24, 23],
    "Marks": [85, 90, 78, 92, 88],
    "Grade": ["B", "A", "C", "A", "B"]
}

df = pd.DataFrame(data)

print("Complete DataFrame:")
print(df)

print("\nSingle column:")
print(df["Name"])

print("\nMultiple columns:")
print(df[["Name", "Marks"]])

print("\nStudents with marks greater than 85:")
print(df[df["Marks"] > 85])

print("\nStudents with marks 90 or more:")
print(df[df["Marks"] >= 90])

print("\nStudents younger than 23:")
print(df[df["Age"] < 23])

print("\nStudents with Grade A:")
print(df[df["Grade"] == "A"])

print("\nStudents with marks greater than 80 and age greater than 22:")
print(df[(df["Marks"] > 80) & (df["Age"] > 22)])