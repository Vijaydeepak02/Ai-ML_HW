##Identify and remove duplicate rows and standardize column formats.##
import pandas as pd

data = {
    "Name": ["Vijay", "Rahul", "John", "Vijay", "David"],
    "Age": ["24", "25", "23", "24", "26"],
    "Marks": ["85", "90", "78", "85", "92"]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

print("\nDuplicate Rows:")
print(df[df.duplicated()])

df = df.drop_duplicates()

df["Age"] = df["Age"].astype(int)
df["Marks"] = df["Marks"].astype(int)

df.columns = df.columns.str.lower()

print("\nCleaned Data:")
print(df)

print("\nData Types:")
print(df.dtypes)