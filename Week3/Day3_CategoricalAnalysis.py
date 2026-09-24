##Analyze categorical features by counts or averages and present the results visually.##
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Department": ["IT", "IT", "HR", "HR", "Sales", "Sales", "IT", "Sales"],
    "Marks": [85, 90, 75, 80, 88, 92, 95, 85]
}

df = pd.DataFrame(data)

print("Category Counts:")
print(df["Department"].value_counts())

print("\nAverage Marks by Department:")
print(df.groupby("Department")["Marks"].mean())

plt.figure(figsize=(7, 5))
sns.countplot(x="Department", data=df)

plt.title("Number of Students by Department")
plt.xlabel("Department")
plt.ylabel("Count")

plt.show()

plt.figure(figsize=(7, 5))
sns.barplot(x="Department", y="Marks", data=df)

plt.title("Average Marks by Department")
plt.xlabel("Department")
plt.ylabel("Average Marks")

plt.show()