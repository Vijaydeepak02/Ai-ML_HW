##Explain the characteristics of each cluster and provide simple business recommendations.##
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.DataFrame({
    "AnnualIncome": [20, 25, 30, 35, 70, 75, 80, 85],
    "SpendingScore": [80, 75, 85, 70, 30, 25, 35, 20]
})

df = df.dropna()

X = df[["AnnualIncome", "SpendingScore"]]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

wcss = []

for k in range(1, 6):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X_scaled)
    wcss.append(model.inertia_)

plt.plot(range(1, 6), wcss, marker="o")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.show()

model = KMeans(n_clusters=2, random_state=42, n_init=10)
df["Cluster"] = model.fit_predict(X_scaled)

print("Customer Clusters:")
print(df)

print("\nCluster Characteristics:")
print(df.groupby("Cluster")[["AnnualIncome", "SpendingScore"]].mean())

for cluster in sorted(df["Cluster"].unique()):
    group = df[df["Cluster"] == cluster]
    income = group["AnnualIncome"].mean()
    spending = group["SpendingScore"].mean()

    print(f"\nCluster {cluster}")
    print(f"Average Income: {income:.2f}")
    print(f"Average Spending Score: {spending:.2f}")

    if income >= 50 and spending >= 50:
        print("Recommendation: Offer premium products and loyalty rewards.")
    elif income >= 50 and spending < 50:
        print("Recommendation: Provide personalized offers to increase spending.")
    elif income < 50 and spending >= 50:
        print("Recommendation: Promote affordable products and reward frequent purchases.")
    else:
        print("Recommendation: Offer budget-friendly deals and discounts.")

plt.scatter(
    df["AnnualIncome"],
    df["SpendingScore"],
    c=df["Cluster"]
)
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")
plt.show()