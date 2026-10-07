##Run a basic GridSearchCV example for one model.##
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

print("Best Parameters:", grid.best_params_)
print("Best Score:", grid.best_score_)