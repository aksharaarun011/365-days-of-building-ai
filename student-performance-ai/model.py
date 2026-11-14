
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# 1. Create student dataset
data = {
    "Study_Hours": [1, 2, 3, 4, 5],
    "Marks": [10, 20, 30, 40, 50]
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

# 7. Test model accuracy
test_predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, test_predictions)
print("Actual Test Marks:", list(y_test))
print("Predicted Test Marks:", test_predictions)
print("Testing MAE:", mae)

mse = mean_squared_error(y_test, test_predictions)
print("Testing MSE:", mse)