##Use cross_val_score to assess model reliability.##
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Attendance": [60, 65, 70, 72, 75, 80, 85, 90, 92, 95],
    "Pass": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Hours", "Attendance"]]
y = df["Pass"]

model = RandomForestClassifier(n_estimators=100, random_state=42)

scores = cross_val_score(model, X, y, cv=5)

print("Cross-validation scores:", scores)
print("Average Score:", scores.mean())