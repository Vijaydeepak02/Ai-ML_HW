##Create a small marks or sales dataset, clean it, analyze it, and produce a summary.##
import pandas as pd
import numpy as np

data = {
    "Name": ["Vijay", "Rahul", "John", "David", "Mike", "Sam"],
    "Math": [85, 90, np.nan, 92, 78, 88],
    "Science": [80, 85, 75, np.nan, 82, 90],
    "English": [90, 88, 82, 95, np.nan, 85]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

df["Math"] = df["Math"].fillna(df["Math"].mean())
df["Science"] = df["Science"].fillna(df["Science"].mean())
df["English"] = df["English"].fillna(df["English"].mean())

df["Total"] = df["Math"] + df["Science"] + df["English"]

df["Percentage"] = (df["Total"] / 300) * 100

df["Result"] = np.where(df["Percentage"] >= 40, "Pass", "Fail")

print("\nCleaned Data:")
print(df)

print("\nAverage Marks:")
print("Math:", df["Math"].mean())
print("Science:", df["Science"].mean())
print("English:", df["English"].mean())

print("\nClass Average Percentage:")
print(df["Percentage"].mean())

print("\nHighest Percentage:")
print(df["Percentage"].max())

print("\nLowest Percentage:")
print(df["Percentage"].min())

print("\nNumber of Students Passed:")
print((df["Result"] == "Pass").sum())

print("\nStudent Summary:")
print(df[["Name", "Total", "Percentage", "Result"]])