##Add clear comments explaining data loading, preprocessing, training, prediction, and evaluation.##
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# 1. Data Loading
# Create a small student dataset
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Attendance": [60, 65, 70, 72, 75, 80, 85, 90, 92, 95],
    "Pass": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)


# 2. Preprocessing
# Separate input features (X) and target (y)
X = df[["Hours", "Attendance"]]
y = df["Pass"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)


# 3. Training
# Create the Logistic Regression model
model = LogisticRegression()

# Train the model using the training data
model.fit(X_train, y_train)


# 4. Prediction
# Use the trained model to predict the test data
y_pred = model.predict(X_test)

print("\nActual Values:")
print(y_test.values)

print("\nPredicted Values:")
print(y_pred)


# 5. Evaluation
# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:")
print(accuracy)

# Display the confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Display precision, recall, and F1-score
print("\nClassification Report:")
print(classification_report(y_test, y_pred))