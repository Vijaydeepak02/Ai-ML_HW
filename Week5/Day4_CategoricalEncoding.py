##Practice label encoding and one-hot encoding for categorical data.##
import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame({
    "Department": ["IT", "HR", "Sales", "IT", "HR"]
})

df["Label_Encoded"] = LabelEncoder().fit_transform(df["Department"])

one_hot = pd.get_dummies(df["Department"], dtype=int)

df = pd.concat([df, one_hot], axis=1)

print(df)