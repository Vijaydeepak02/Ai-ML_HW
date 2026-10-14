##Apply clustering to a small real-world customer or student dataset.##
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = {
    "Age": [20, 22, 25, 45, 48, 50, 30, 32],
    "Spending": [80, 85, 90, 30, 35, 25, 70, 75]
}

df = pd.DataFrame(data)

X = df[["Age", "Spending"]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = KMeans(n_clusters=2, random_state=42, n_init=10)
df["Cluster"] = model.fit_predict(X_scaled)

print("Customer Dataset with Clusters:")
print(df)

print("\nCluster Analysis:")
print(df.groupby("Cluster")[["Age", "Spending"]].mean())