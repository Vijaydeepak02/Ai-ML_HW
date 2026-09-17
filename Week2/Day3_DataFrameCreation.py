##Create DataFrames from dictionaries and lists and inspect rows and columns.##
import pandas as pd

data_dict = {
    "Name": ["John", "Mike", "Sarah", "David"],
    "Age": [22, 25, 21, 24],
    "Marks": [85, 90, 78, 92]
}

df1 = pd.DataFrame(data_dict)

print("DataFrame from dictionary:")
print(df1)

data_list = [
    ["John", 22, 85],
    ["Mike", 25, 90],
    ["Sarah", 21, 78],
    ["David", 24, 92]
]

df2 = pd.DataFrame(
    data_list,
    columns=["Name", "Age", "Marks"]
)

print("\nDataFrame from list:")
print(df2)

print("\nFirst 2 rows:")
print(df1.head(2))

print("\nLast 2 rows:")
print(df1.tail(2))

print("\nRows:")
print(df1.index)

print("\nColumns:")
print(df1.columns)

print("\nShape:")
print(df1.shape)

print("\nData types:")
print(df1.dtypes)

print("\nName column:")
print(df1["Name"])

print("\nMarks column:")
print(df1["Marks"])