
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

data = {
    "Study_Hours": [
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10,
        2, 4, 6, 8, 10
    ],
    "Marks": [
        12, 20, 29, 38, 51,
        59, 68, 82, 89, 98,
        22, 41, 61, 79, 96
    ]
}

df = pd.DataFrame(data)

# 2. Separate input and output
X = df[["Study_Hours"]]
y = df["Marks"]

# 3. Create the Linear Regression model
model = LinearRegression()

# 4. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5. Train the model
model.fit(X_train, y_train)

# 5. Display model details
print("Model Training Completed!")
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# 6. Predict marks for a new student
new_student = pd.DataFrame({"Study_Hours": [7]})
prediction = model.predict(new_student)
print("Predicted Marks for 7 hours:", prediction[0])

# Make predictions on test data
test_predictions = model.predict(X_test)

# Calculate evaluation metrics
mae = mean_absolute_error(y_test, test_predictions)
mse = mean_squared_error(y_test, test_predictions)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, test_predictions)

# Display results
print("\nModel Evaluation Results")
print("Actual Test Marks:", list(y_test))
print("Predicted Test Marks:", test_predictions)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)