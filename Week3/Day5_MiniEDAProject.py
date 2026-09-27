##Perform exploratory data analysis on a sample CSV dataset and include charts and findings.##
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nAverage Marks:")
print(df[["Math", "Science", "English"]].mean())

print("\nAverage Marks by Department:")
print(df.groupby("Department")[["Math", "Science", "English"]].mean())

plt.figure(figsize=(7, 5))
sns.countplot(x="Department", data=df)
plt.title("Students by Department")
plt.xlabel("Department")
plt.ylabel("Number of Students")
plt.show()

plt.figure(figsize=(7, 5))
sns.histplot(df["Math"], bins=5, kde=True)
plt.title("Distribution of Math Marks")
plt.xlabel("Math Marks")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(7, 5))
sns.boxplot(x="Department", y="Math", data=df)
plt.title("Math Marks by Department")
plt.xlabel("Department")
plt.ylabel("Math Marks")
plt.show()

plt.figure(figsize=(7, 5))
sns.scatterplot(x="Math", y="Science", data=df)
plt.title("Math vs Science")
plt.xlabel("Math Marks")
plt.ylabel("Science Marks")
plt.show()

plt.figure(figsize=(7, 5))
sns.heatmap(df[["Math", "Science", "English"]].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Between Subjects")
plt.show()