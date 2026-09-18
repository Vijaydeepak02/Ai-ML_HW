##Create new columns based on calculations from existing columns, such as total marks or percentages.##
import pandas as pd

data = {
    "Name": ["Vijay", "Rahul", "John", "David", "Mike"],
    "Math": [85, 90, 78, 92, 88],
    "Science": [80, 85, 75, 89, 90],
    "English": [90, 88, 82, 95, 85]
}

df = pd.DataFrame(data)

df["Total_Marks"] = df["Math"] + df["Science"] + df["English"]

df["Percentage"] = (df["Total_Marks"] / 300) * 100

print(df)