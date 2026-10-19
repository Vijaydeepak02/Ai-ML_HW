##Change epochs or hidden-layer settings and observe performance changes.##
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

settings = [
    ((5,), 500),
    ((10,), 1000),
    ((20, 10), 1500)
]

for layers, epochs in settings:
    model = MLPClassifier(
        hidden_layer_sizes=layers,
        max_iter=epochs,
        random_state=42
    )
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print("Hidden Layers:", layers)
    print("Max Iterations:", epochs)
    print("Accuracy:", accuracy_score(y_test, predictions))
    print()