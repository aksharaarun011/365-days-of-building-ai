import pandas as pd
import numpy as np

# Creating raw student dataset
data = {
    "Student": ["A", "B", "C", "D", "E",
                "F", "G", "H", "I", "J"],

    "Study_Hours": [2, 3, np.nan, 5, 20,
                    4, 6, 3, 8, 2],

    "Marks": [40, 50, 60, np.nan, 95,
              55, 70, 45, 85, 40],

    "Subject": ["Maths", "Science", "English",
                "Maths", "Science", "English",
                "Maths", "Science", "English", "Maths"]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())

# Handling missing values

df["Study_Hours"] = df["Study_Hours"].fillna(
    df["Study_Hours"].mean()
)

df["Marks"] = df["Marks"].fillna(
    df["Marks"].mean()
)

print("\nDataset after handling missing values:")
print(df)

print("\nMissing Values after Cleaning:")
print(df.isnull().sum())

# Detecting outliers using IQR

Q1 = df["Study_Hours"].quantile(0.25)
Q3 = df["Study_Hours"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("\nQ1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)

print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

# Displaying outliers
outliers = df[
    (df["Study_Hours"] < lower_bound) |
    (df["Study_Hours"] > upper_bound)
]

print("\nDetected Outliers:")
print(outliers)

# Capping outliers
df["Study_Hours"] = df["Study_Hours"].clip(
    lower=lower_bound,
    upper=upper_bound
)

print("\nDataset after handling outliers:")
print(df)

# One-Hot Encoding

df = pd.get_dummies(df, columns=["Subject"], dtype=int)

print("\nDataset after One-Hot Encoding:")
print(df)

# Feature Scaling

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

df[["Study_Hours", "Marks"]] = scaler.fit_transform(
    df[["Study_Hours", "Marks"]]
)

print("\nFinal Preprocessed Dataset:")
print(df)

# Final Dataset Verification

print("\nFinal Dataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nFinal Dataset Shape:")
print(df.shape)