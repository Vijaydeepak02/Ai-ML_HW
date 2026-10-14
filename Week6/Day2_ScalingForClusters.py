##Compare clustering results before and after feature scaling.##
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = {
    "Hours": [1, 2, 3, 8, 9, 10],
    "Marks": [20, 25, 30, 80, 85, 90]
}

df = pd.DataFrame(data)
X = df[["Hours", "Marks"]]

model1 = KMeans(n_clusters=2, random_state=42, n_init=10)
df["Before Scaling"] = model1.fit_predict(X)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model2 = KMeans(n_clusters=2, random_state=42, n_init=10)
df["After Scaling"] = model2.fit_predict(X_scaled)

print(df)