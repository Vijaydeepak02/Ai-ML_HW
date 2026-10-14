##Test different K values and use the elbow plot to choose a suitable number of clusters.##
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = {
    "Hours": [1, 2, 3, 8, 9, 10],
    "Marks": [20, 25, 30, 80, 85, 90]
}

df = pd.DataFrame(data)

wcss = []

for k in range(1, 6):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(df)
    wcss.append(model.inertia_)

plt.plot(range(1, 6), wcss, marker="o")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.show()