##Rename columns and sort records based on values in one or more columns.##
import pandas as pd
import numpy as np

data = {
    "Name": ["Vijay", "Rahul", "John", "David", "Mike"],
    "Age": [24, np.nan, 23, 26, np.nan],
    "Marks": [85, 90, np.nan, 92, 88]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nMissing Values:")
print(df.isnull())

print("\nNumber of Missing Values:")
print(df.isnull().sum())

df_filled = df.fillna(0)

print("\nMissing Values Filled with 0:")
print(df_filled)

df_age_filled = df.copy()
df_age_filled["Age"] = df_age_filled["Age"].fillna(df_age_filled["Age"].mean())

print("\nAge Missing Values Filled with Mean:")
print(df_age_filled)

df_dropped = df.dropna()

print("\nRows with Missing Values Dropped:")
print(df_dropped)