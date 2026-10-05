##Week4##
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["vijay","Deepak","sai","rahul","raju"],
    "Marks": [80,65,75,92,45]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\n Average of marks", df["Marks"].mean())
print("\n Highest", df["Marks"].max())
print("\n Lowest", df["Marks"].min())

plt.bar(df["Name"], df["Marks"])

plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("marks")

plt.show()