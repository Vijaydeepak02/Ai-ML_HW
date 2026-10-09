##Write one script that handles the complete machine learning workflow from raw data to evaluation.##
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.DataFrame({
    "Age": [22, 25, None, 30, 28, 35, 24, 32, 27, 40],
    "Salary": [30000, 40000, 35000, 50000, 45000, 60000, 32000, 55000, 42000, 65000],
    "Passed": [0, 0, 1, 1, 1, 1, 0, 1, 0, 1]
})

print("Raw Data:")
print(df)

X = df[["Age", "Salary"]]
y = df["Passed"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

model = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression())
])

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nActual Values:", y_test.values)
print("Predicted Values:", y_pred)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))