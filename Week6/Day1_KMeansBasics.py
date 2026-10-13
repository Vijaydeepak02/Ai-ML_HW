##Apply KMeans clustering to sample data and inspect cluster assignments.##
import pandas as pd
from sklearn.cluster import KMeans

data = {
    "Hours": [1, 2, 3, 8, 9, 10],
    "Marks": [20, 25, 30, 80, 85, 90]
}

df = pd.DataFrame(data)

model = KMeans(n_clusters=2, random_state=42, n_init=10)

model.fit(df)

df["Cluster"] = model.labels_

print("Cluster Assignments:")
print(df)