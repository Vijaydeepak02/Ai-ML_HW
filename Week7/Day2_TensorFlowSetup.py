##Install TensorFlow and understand the structure of a simple Sequential model.##
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential([
    Dense(8, activation="relu", input_shape=(4,)),
    Dense(3, activation="softmax")
])

model.summary()