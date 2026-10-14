##Add cluster labels to the dataset and analyze each cluster group.##
import pandas as pd
from sklearn.cluster import KMeans

data = {
    "Hours": [1, 2, 3, 8, 9, 10],
    "Marks": [20, 25, 30, 80, 85, 90]
}

df = pd.DataFrame(data)

model = KMeans(n_clusters=2, random_state=42, n_init=10)
df["Cluster"] = model.fit_predict(df[["Hours", "Marks"]])

print("Dataset with Cluster Labels:")
print(df)

print("\nCluster Analysis:")
print(df.groupby("Cluster")[["Hours", "Marks"]].mean())
