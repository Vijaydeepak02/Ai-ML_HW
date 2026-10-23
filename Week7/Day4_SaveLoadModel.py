##Save the trained model and reload it for prediction.##
import joblib
from sklearn.tree import DecisionTreeClassifier

X = [[2], [4], [6], [8], [10]]
y = [0, 0, 1, 1, 1]

model = DecisionTreeClassifier()
model.fit(X, y)

joblib.dump(model, "model.pkl")

loaded_model = joblib.load("model.pkl")

print("Prediction:", loaded_model.predict([[7]]))