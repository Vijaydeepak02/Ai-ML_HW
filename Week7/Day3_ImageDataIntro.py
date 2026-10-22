##Load an image dataset such as MNIST and inspect features and labels.##
import tensorflow as tf
import matplotlib.pyplot as plt

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

print("Feature shape:", X_train.shape)
print("Label:", y_train[0])

plt.imshow(X_train[0], cmap="gray")
plt.title(f"Digit: {y_train[0]}")
plt.show()