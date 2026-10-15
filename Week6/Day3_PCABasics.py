##Learn dimensionality reduction basics and apply PCA to a dataset.##
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

data = {
    "Age": [20, 22, 25, 45, 48, 50],
    "Spending": [80, 85, 90, 30, 35, 25],
    "Income": [20000, 25000, 30000, 60000, 65000, 70000]
}

df = pd.DataFrame(data)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print("Original Shape:", df.shape)
print("Reduced Shape:", X_pca.shape)
print("PCA Data:")
print(X_pca)
print("Explained Variance:", pca.explained_variance_ratio_)