##Write five key observations about a dataset and support them with charts.##
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Department": ["IT", "IT", "HR", "HR", "Sales", "Sales", "IT", "Sales"],
    "Math": [85, 90, 75, 80, 88, 92, 95, 85],
    "Science": [80, 85, 78, 90, 72, 94, 82, 89],
    "Age": [22, 24, 23, 25, 26, 24, 23, 27]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\nFive Key Observations:")

print("1. IT has the highest number of students.")
print("2. Sales has the highest average Math marks.")
print("3. Science marks are generally close to Math marks.")
print("4. Student ages range from 22 to 27.")
print("5. Math and Science marks show a positive relationship.")

plt.figure(figsize=(7, 5))
sns.countplot(x="Department", data=df)
plt.title("Students by Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(7, 5))
sns.barplot(x="Department", y="Math", data=df)
plt.title("Average Math Marks by Department")
plt.xlabel("Department")
plt.ylabel("Average Math Marks")
plt.show()

plt.figure(figsize=(7, 5))
sns.histplot(df["Age"], bins=5)
plt.title("Distribution of Student Age")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(7, 5))
sns.scatterplot(x="Math", y="Science", data=df)
plt.title("Math vs Science Marks")
plt.xlabel("Math Marks")
plt.ylabel("Science Marks")
plt.show()

plt.figure(figsize=(7, 5))
sns.boxplot(x="Department", y="Math", data=df)
plt.title("Math Marks Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Math Marks")
plt.show()