##Create pandas Series objects and practice indexing, filtering, and value access.##
import pandas as pd

marks = pd.Series(
    [85, 90, 78, 92, 88],
    index=["John", "Mike", "Sarah", "David", "Lisa"]
)

print("Student Marks:")
print(marks)

print("\nJohn's marks:")
print(marks["John"])

print("\nSarah's marks using loc:")
print(marks.loc["Sarah"])

print("\nFirst student's marks using iloc:")
print(marks.iloc[0])

print("\nJohn, Sarah and Lisa's marks:")
print(marks.loc[["John", "Sarah", "Lisa"]])

print("\nStudents with marks greater than 85:")
print(marks[marks > 85])

print("\nStudents with marks 90 or more:")
print(marks[marks >= 90])

print("\nStudents with marks less than 80:")
print(marks[marks < 80])

print("\nValues:")
print(marks.values)

print("\nIndex labels:")
print(marks.index)

print("\nNumber of students:")
print(len(marks))

print("\nAverage marks:")
print(marks.mean())