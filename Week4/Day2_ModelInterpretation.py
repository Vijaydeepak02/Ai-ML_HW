##Write brief notes explaining coefficients, predictions, and model behavior.##
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [40, 45, 50, 55, 65, 70, 80, 90]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Coefficient:", model.coef_[0])
print("Predictions:", y_pred)

# Notes

# Coefficient:
# The coefficient shows how much Marks change when Hours increase by 1.

# Predictions:
# Predictions are the Marks estimated by the trained model.

# Model Behavior:
# The model learns the relationship between Hours and Marks.
# As Hours increase, predicted Marks also increase.
# Predictions may not exactly match the actual Marks.