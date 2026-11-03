import pandas as pd

#create a dataset with missing vlaues
data={
    "Student":["A","B","C","D","E"],
    "Study_Hours":[1,2,None,4,5],
    "Marks":[10,20,30,None,50]
}

#convert into dataframe
df=pd.DataFrame(data)

#display the dataset
print("Original Dataset:")
print(df)

#Identify missing values
print("Missing Values:")
print(df.isnull())
#count missing values
print("\n missing values count:")
print(df.isnull().sum())

# Remove rows containing missing values
cleaned_df = df.dropna()
print("\nDataset after removing missing values:")
print(cleaned_df)

# Calculate the mean of each numerical column
study_hours_mean = df["Study_Hours"].mean()
marks_mean = df["Marks"].mean()

# Replace missing values with their respective means
df["Study_Hours"] = df["Study_Hours"].fillna(study_hours_mean)
df["Marks"] = df["Marks"].fillna(marks_mean)

# Display the updated dataset
print("\nDataset after filling missing values:")
print(df)