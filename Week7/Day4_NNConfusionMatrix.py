##Create a confusion matrix for the neural network predictions.##
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

predictions = model.predict(X_test, verbose=0).argmax(axis=1)

cm = confusion_matrix(y_test, predictions)

display = ConfusionMatrixDisplay(confusion_matrix=cm)
display.plot(cmap="Blues")
plt.title("Neural Network Confusion Matrix")
plt.show()
