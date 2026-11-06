import pandas as pd

# Creating a dataset
data = {
    "Student": ["A", "B", "C", "D", "E",
                "F", "G", "H", "I"],
    "Study_Hours": [2, 3, 3, 4, 4, 5, 5, 6, 20]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Calculating quartiles
Q1 = df["Study_Hours"].quantile(0.25)
Q3 = df["Study_Hours"].quantile(0.75)

# Calculating IQR
IQR = Q3 - Q1

print("\nQ1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)

# Calculating outlier boundaries
lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)

print("\nLower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

# Identifying outliers
outliers = df[
    (df["Study_Hours"] < lower_bound) |
    (df["Study_Hours"] > upper_bound)
]

print("\nDetected Outliers:")
print(outliers)

import matplotlib.pyplot as plt

# Creating a boxplot
plt.boxplot(df["Study_Hours"])

plt.title("Boxplot of Study Hours")
plt.ylabel("Study Hours")

plt.show()

# Creating a copy of the dataset
df_capped = df.copy()

# Capping outliers
df_capped["Study_Hours"] = df_capped["Study_Hours"].clip(
    lower=lower_bound,
    upper=upper_bound
)

print("\nDataset after Capping:")
print(df_capped)