##Adjust epochs, hidden units, or layers to try improving model performance.##
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

X_train = X_train / 255.0
X_test = X_test / 255.0

settings = [
    (64, 1, 5),
    (128, 1, 10),
    (128, 2, 10)
]

for units, layers, epochs in settings:
    model = Sequential([Flatten(input_shape=(28, 28))])

    for _ in range(layers):
        model.add(Dense(units, activation="relu"))

    model.add(Dense(10, activation="softmax"))

    model.compile(optimizer="adam",
                  loss="sparse_categorical_crossentropy",
                  metrics=["accuracy"])

    model.fit(X_train, y_train, epochs=epochs, verbose=0)

    loss, accuracy = model.evaluate(X_test, y_test, verbose=0)

    print("Hidden Units:", units)
    print("Hidden Layers:", layers)
    print("Epochs:", epochs)
    print("Test Accuracy:", accuracy)
    print()