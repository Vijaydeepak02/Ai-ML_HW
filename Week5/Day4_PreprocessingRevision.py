##Repeat missing-value handling, encoding, scaling, and splitting in one full workflow.##
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

data = {
    "Age": [22, 25, None, 30, 28, 35],
    "Salary": [30000, 40000, 35000, None, 50000, 60000],
    "Department": ["IT", "HR", "IT", "HR", "Sales", "IT"],
    "Passed": [1, 0, 1, 0, 1, 1]
}

df = pd.DataFrame(data)

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

df["Department"] = LabelEncoder().fit_transform(df["Department"])

X = df[["Age", "Salary", "Department"]]
y = df["Passed"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("X_train:", X_train)
print("X_test:", X_test)
print("y_train:", y_train.values)
print("y_test:", y_test.values)