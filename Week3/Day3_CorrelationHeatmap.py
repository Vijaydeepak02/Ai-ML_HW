##Create a correlation matrix and visualize it with a heatmap.##
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Math": [85, 90, 75, 88, 70, 95, 80, 92],
    "Science": [80, 85, 78, 90, 72, 94, 82, 89],
    "English": [90, 88, 82, 95, 75, 92, 85, 91],
    "Computer": [95, 92, 80, 90, 78, 96, 88, 94]
}

df = pd.DataFrame(data)

correlation = df.corr()

print(correlation)

plt.figure(figsize=(8, 6))

sns.heatmap(correlation, annot=True, cmap="coolwarm")

plt.title("Correlation Matrix Heatmap")

plt.show()