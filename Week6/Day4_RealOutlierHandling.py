##Remove or cap outliers and compare the change in results.##
import pandas as pd

df = pd.DataFrame({
    "Marks": [45, 50, 55, 60, 65, 70, 75, 200]
})

Q1 = df["Marks"].quantile(0.25)
Q3 = df["Marks"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df["Capped"] = df["Marks"].clip(lower, upper)
removed = df[(df["Marks"] >= lower) & (df["Marks"] <= upper)]

print("Original Average:", df["Marks"].mean())
print("Capped Average:", df["Capped"].mean())
print("Average After Removing Outliers:", removed["Marks"].mean())

print("\nCapped Data:")
print(df)

print("\nData After Removing Outliers:")
print(removed)