##Identify independent and dependent variables in a machine learning dataset.##
import pandas as pd

data = {
    "Hours_Studied": [2, 3, 4, 5, 6],
    "Attendance": [70, 75, 80, 85, 90],
    "Marks": [50, 60, 70, 80, 90]
}

df = pd.DataFrame(data)

X = df[["Hours_Studied", "Attendance"]]
y = df["Marks"]

print("Independent Variables:")
print(X)

print("\nDependent Variable:")
print(y)