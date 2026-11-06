import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Create a dataset
data = {
    "Student": ["A", "B", "C", "D", "E"],
    "Study_Hours": [2, 3, 4, 5, 6],
    "Favourite_Subject": [
        "Maths",
        "Science",
        "English",
        "Maths",
        "Science"
    ]
}

# Convert into DataFrame
df = pd.DataFrame(data)

print("Original Dataset:")
print(df)


# Create a LabelEncoder object
encoder = LabelEncoder()

# Encode the Favourite_Subject column
df["Subject_Encoded"] = encoder.fit_transform(
    df["Favourite_Subject"]
)

print("\nDataset after Label Encoding:")
print(df)

# Apply One-Hot Encoding
one_hot_encoded = pd.get_dummies(
    df,
    columns=["Favourite_Subject"],
    dtype=int
)

print("\nDataset after One-Hot Encoding:")
print(one_hot_encoded)