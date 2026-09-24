##Use box plots and the IQR method to detect outliers.##
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Marks": [50, 55, 60, 62, 65, 68, 70, 72, 75, 78, 80, 150]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

Q1 = df["Marks"].quantile(0.25)
Q3 = df["Marks"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

print("\nQ1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)

outliers = df[(df["Marks"] < lower_limit) | (df["Marks"] > upper_limit)]

print("\nOutliers:")
print(outliers)

plt.figure(figsize=(7, 5))
sns.boxplot(x=df["Marks"])

plt.title("Box Plot for Outlier Detection")
plt.xlabel("Marks")

plt.show()