##Convert strings to numeric values, parse dates, and adjust category types.##
import pandas as pd

data = {
    "Name": ["Vijay", "Rahul", "John", "David"],
    "Age": ["24", "25", "23", "26"],
    "Salary": ["50000", "55000", "48000", "60000"],
    "Join_Date": ["2026-01-10", "2026-02-15", "2026-03-20", "2026-04-05"],
    "Department": ["IT", "HR", "IT", "Sales"]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)
print(df.dtypes)

df["Age"] = pd.to_numeric(df["Age"])
df["Salary"] = pd.to_numeric(df["Salary"])

df["Join_Date"] = pd.to_datetime(df["Join_Date"])

df["Department"] = df["Department"].astype("category")

print("\nConverted Data:")
print(df)
print(df.dtypes)