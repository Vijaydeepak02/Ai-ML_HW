##Analyze the distribution of numerical columns and interpret mean/median behavior.##
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Math": [60, 65, 70, 75, 80, 85, 90, 95],
    "Science": [55, 60, 65, 70, 75, 80, 85, 90],
    "English": [70, 72, 75, 78, 80, 82, 85, 88]
}

df = pd.DataFrame(data)

print("Mean:")
print(df.mean())

print("\nMedian:")
print(df.median())

print("\nStatistics:")
print(df.describe())

plt.figure(figsize=(8, 5))
sns.histplot(df["Math"], bins=5, kde=True)

plt.title("Distribution of Math Marks")
plt.xlabel("Math Marks")
plt.ylabel("Frequency")

plt.grid(True)
plt.show()