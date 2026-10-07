##Inspect the best parameters and explain why they may improve performance.##
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Attendance": [60, 65, 70, 72, 75, 80, 85, 90, 92, 95],
    "Pass": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Hours", "Attendance"]]
y = df["Pass"]

model = RandomForestClassifier(random_state=42)

parameters = {
    "n_estimators": [50, 100],
    "max_depth": [2, 3, 4]
}

grid = GridSearchCV(model, parameters, cv=3)

grid.fit(X, y)

print("Best Parameters:")
print(grid.best_params_)

print("\nBest Score:")
print(grid.best_score_)

print("\nWhy these parameters may improve performance:")

if grid.best_params_["n_estimators"] == 100:
    print("- More trees can make predictions more stable.")

if grid.best_params_["max_depth"] <= 3:
    print("- Smaller tree depth can reduce overfitting.")
else:
    print("- Greater tree depth allows the model to learn more complex patterns.")