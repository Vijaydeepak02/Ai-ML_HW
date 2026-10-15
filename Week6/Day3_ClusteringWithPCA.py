##Run KMeans on PCA-transformed data and compare the clusters.##
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

iris = load_iris()
X = iris.data

X_scaled = StandardScaler().fit_transform(X)

model1 = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters_original = model1.fit_predict(X_scaled)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

model2 = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters_pca = model2.fit_predict(X_pca)

print("Original Data Clusters:")
print(clusters_original)

print("\nPCA Data Clusters:")
print(clusters_pca)

print("\nVariance Retained:", pca.explained_variance_ratio_.sum() * 100, "%")