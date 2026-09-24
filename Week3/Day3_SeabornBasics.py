##Practice count plots, box plots, and pair plots using a sample dataset.##
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("iris")

plt.figure(figsize=(7, 5))
sns.countplot(x="species", data=data)
plt.title("Count of Each Species")
plt.xlabel("Species")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(7, 5))
sns.boxplot(x="species", y="sepal_length", data=data)
plt.title("Sepal Length by Species")
plt.xlabel("Species")
plt.ylabel("Sepal Length")
plt.show()

sns.pairplot(data, hue="species")
plt.show()