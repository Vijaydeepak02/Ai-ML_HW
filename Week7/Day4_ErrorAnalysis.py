##Inspect wrong predictions and suggest possible reasons for the errors.##
import matplotlib.pyplot as plt
import numpy as np

predictions = model.predict(X_test, verbose=0).argmax(axis=1)
wrong = np.where(predictions != y_test)[0]

for i in wrong[:5]:
    plt.imshow(X_test[i], cmap="gray")
    plt.title(f"Actual: {y_test[i]}, Predicted: {predictions[i]}")
    plt.show()

    print("Possible reason: Similar digit shape, unclear handwriting, or unusual writing style.")