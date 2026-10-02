##Apply scaling with StandardScaler or MinMaxScaler and compare results.##
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import accuracy_score

data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Attendance": [60, 65, 70, 72, 75, 80, 85, 90, 92, 95],
    "Pass": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Hours", "Attendance"]]
y = df["Pass"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = KNeighborsClassifier(n_neighbors=5)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy without scaling:", accuracy)


standard = StandardScaler()

X_train_std = standard.fit_transform(X_train)
X_test_std = standard.transform(X_test)

model_std = KNeighborsClassifier(n_neighbors=5)

model_std.fit(X_train_std, y_train)

y_pred_std = model_std.predict(X_test_std)

accuracy_std = accuracy_score(y_test, y_pred_std)

print("Accuracy with StandardScaler:", accuracy_std)


minmax = MinMaxScaler()

X_train_min = minmax.fit_transform(X_train)
X_test_min = minmax.transform(X_test)

model_min = KNeighborsClassifier(n_neighbors=5)

model_min.fit(X_train_min, y_train)

y_pred_min = model_min.predict(X_test_min)

accuracy_min = accuracy_score(y_test, y_pred_min)

print("Accuracy with MinMaxScaler:", accuracy_min)