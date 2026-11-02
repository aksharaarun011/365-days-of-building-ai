import pandas as pd

# Create a dataset
data = {
    "Student": ["A", "B", "C", "D", "E"],
    "Study_Hours": [1, 2, 3, 4, 5],
    "Marks": [10, 20, 30, 40, 50]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Display the dataset
print(df)

# Display the first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Display the last 5 rows
print("\nLast 5 rows:")
print(df.tail())

# Display the number of rows and columns
print("\nDataset shape:")
print(df.shape)

# Display column names
print("\nColumn names:")
print(df.columns)

# Display dataset information
print("\nDataset Information:")
df.info()

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Select the Study_Hours column
print("\nStudy Hours:")
print(df["Study_Hours"])

# Select the Marks column
print("\nMarks:")
print(df["Marks"])

# Select multiple columns
print("\nFeatures and Target:")
print(df[["Study_Hours", "Marks"]])

#separate features and target
X=df[["Study_Hours"]]
y=df["Marks"]

# Display features and target
print("\nFeatures (X):")
print(X)

print("\nTarget (y):")
print(y)

#calculate average marks
average_marks=df["Marks"].mean()
print("\n average marks=",average_marks)