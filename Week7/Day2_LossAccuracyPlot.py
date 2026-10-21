##Plot training loss and accuracy from the model history.##
import matplotlib.pyplot as plt

history = model.fit(X_train, y_train, epochs=50, verbose=0)

plt.plot(history.history["loss"])
plt.title("Training Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.show()

plt.plot(history.history["accuracy"])
plt.title("Training Accuracy")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.show()