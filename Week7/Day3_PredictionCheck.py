##Review sample predictions and identify correct and incorrect cases.##
import numpy as np
import matplotlib.pyplot as plt

predictions = model.predict(X_test[:10], verbose=0).argmax(axis=1)

for i in range(10):
    print("Actual:", y_test[i], "Predicted:", predictions[i])

    if y_test[i] == predictions[i]:
        print("Correct Prediction")
    else:
        print("Incorrect Prediction")

    plt.imshow(X_test[i], cmap="gray")
    plt.title(f"Actual: {y_test[i]}, Predicted: {predictions[i]}")
    plt.show()