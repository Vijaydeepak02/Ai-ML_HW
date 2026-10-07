##Extract and visualize important features from the trained model.##
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Attendance": [60, 65, 70, 72, 75, 80, 85, 90],
    "Pass": [0, 0, 0, 0, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Hours", "Attendance"]]
y = df["Pass"]

model = RandomForestClassifier(n_estimators=100, random_state=42)

model.fit(X, y)

importance = model.feature_importances_

print("Feature Importance:")
for feature, value in zip(X.columns, importance):
    print(feature, ":", value)

plt.bar(X.columns, importance)
plt.title("Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.show()