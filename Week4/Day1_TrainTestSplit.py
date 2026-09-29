##Load a small dataset, separate features and target, and apply train_test_split.##
import pandas as pd
from sklearn.model_selection import train_test_split

data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Attendance": [60, 65, 70, 75, 80, 85, 90, 95],
    "Marks": [45, 50, 55, 60, 65, 70, 80, 90]
}

df = pd.DataFrame(data)

X = df[["Hours", "Attendance"]]
y = df["Marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

print("X_train:")
print(X_train)

print("\nX_test:")
print(X_test)

print("\ny_train:")
print(y_train)

print("\ny_test:")
print(y_test)