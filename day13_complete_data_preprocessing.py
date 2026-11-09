import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Creating a dataset
data = {
    "Student": ["A", "B", "C", "D", "E", "E"],
    "Study_Hours": [2, 3, np.nan, 5, 20, 20],
    "Marks": [40, 50, 60, np.nan, 95, 95],
    "Favourite_Subject": [
        "Maths", "Science", "English",
        "Maths", "Science", "Science"
    ]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Exploring the dataset
print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDataset Shape:")
print(df.shape)

# Filling missing numerical values with mean
df["Study_Hours"] = df["Study_Hours"].fillna(
    df["Study_Hours"].mean()
)

df["Marks"] = df["Marks"].fillna(
    df["Marks"].mean()
)

print("\nDataset after handling missing values:")
print(df)

# Checking duplicate records
print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())

# Removing duplicate records
df = df.drop_duplicates()

print("\nDataset after removing duplicates:")
print(df)

# Calculating Q1, Q3 and IQR
Q1 = df["Study_Hours"].quantile(0.25)
Q3 = df["Study_Hours"].quantile(0.75)

IQR = Q3 - Q1

# Calculating boundaries
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("\nLower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

# Capping outliers
df["Study_Hours"] = df["Study_Hours"].clip(
    lower=lower_bound,
    upper=upper_bound
)

print("\nDataset after handling outliers:")
print(df)

# Applying One-Hot Encoding
df = pd.get_dummies(
    df,
    columns=["Favourite_Subject"],
    dtype=int
)

print("\nDataset after One-Hot Encoding:")
print(df)

# Selecting numerical columns
scaler = MinMaxScaler()

df[["Study_Hours", "Marks"]] = scaler.fit_transform(
    df[["Study_Hours", "Marks"]]
)

print("\nFinal Preprocessed Dataset:")
print(df)

# Final verification
print("\nFinal Dataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nFinal Dataset Shape:")
print(df.shape)