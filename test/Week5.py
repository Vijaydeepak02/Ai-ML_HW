import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.DataFrame({
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Attendance": [60, 65, 70, 72, 75, 80, 85, 90, 92, 95],
    "Pass": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
})

x = df[["Hours", "Attendance"]]
y = df["Pass"]

x_train, x_test, y_train, y_test = train_test_split( x, y, test_size=0.3, random_state=42, stratify=y)

model = LogisticRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("Actual:", y_test.values)
print("Predicted:", y_pred)
print("Accuracy:", accuracy_score(y_test, y_pred)) 








