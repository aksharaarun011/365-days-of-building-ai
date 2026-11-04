import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Create a student dataset
data = {
    "Student": ["A", "B", "C", "D", "E"],
    "Study_Hours": [1, 2, 3, 4, 5],
    "Marks": [10, 20, 30, 40, 50]
}

# Convert into a DataFrame
df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Create a MinMaxScaler object
scaler = MinMaxScaler()

# Apply scaling to numerical columns
df[["Study_Hours", "Marks"]] = scaler.fit_transform(
    df[["Study_Hours", "Marks"]]
)

print("\nDataset after Min-Max Scaling:")
print(df)


from sklearn.preprocessing import StandardScaler

# Create a fresh dataset
original_df = pd.DataFrame(data)

# Create a StandardScaler object
standard_scaler = StandardScaler()

# Apply standardization
standardized_data = standard_scaler.fit_transform(
    original_df[["Study_Hours", "Marks"]]
)

# Convert the result into a DataFrame
standardized_df = pd.DataFrame(
    standardized_data,
    columns=["Study_Hours", "Marks"]
)

print("\nDataset after Standardization:")
print(standardized_df)