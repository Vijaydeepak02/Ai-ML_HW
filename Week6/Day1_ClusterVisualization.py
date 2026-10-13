##Create a scatter plot that shows clusters clearly for a two-feature dataset.##
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = {
    "Hours": [1, 2, 3, 8, 9, 10],
    "Marks": [20, 25, 30, 80, 85, 90]
}

df = pd.DataFrame(data)

model = KMeans(n_clusters=2, random_state=42, n_init=10)
model.fit(df)

df["Cluster"] = model.labels_

plt.scatter(df["Hours"], df["Marks"], c=df["Cluster"])
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.title("KMeans Clustering")
plt.show()