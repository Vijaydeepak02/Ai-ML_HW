##Use a customer dataset for cleaning, scaling, clustering, elbow analysis, and cluster interpretation.##
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.DataFrame({
    "AnnualIncome": [20, 25, 30, 35, 70, 75, 80, 85],
    "SpendingScore": [80, 75, 85, 70, 30, 25, 35, 20]
})

df = df.dropna()
X = StandardScaler().fit_transform(df)

wcss = []
for k in range(1, 6):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X)
    wcss.append(model.inertia_)

plt.plot(range(1, 6), wcss, marker="o")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.show()

model = KMeans(n_clusters=2, random_state=42, n_init=10)
df["Cluster"] = model.fit_predict(X)

print(df)
print(df.groupby("Cluster").mean())