##Maintain a table comparing models and their accuracy scores.##
import pandas as pd

models = {
    "Model": [
        "Decision Tree",
        "Random Forest",
        "Logistic Regression",
        "KNN"
    ],
    "Accuracy": [
        0.85,
        0.92,
        0.88,
        0.86
    ]
}

results = pd.DataFrame(models)

print(results)