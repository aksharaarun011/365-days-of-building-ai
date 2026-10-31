
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


# 1. Create input data (hours studied)
X = np.array([[1], [2], [3], [4], [5], [6]])

# 2. Create actual scores
y = np.array([10, 20, 30, 40, 50, 60])


# 3. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training data:", X_train.flatten())
print("Testing data:", X_test.flatten())

# 4. Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# 5. Predict scores using testing data
predictions = model.predict(X_test)

# 6. Calculate prediction errors
errors = y_test - predictions

# 7. Calculate Mean Absolute Error (MAE)
mae = mean_absolute_error(y_test, predictions)

# 8. Display results
print("\nActual test scores:", y_test)
print("Predicted test scores:", predictions.round(2))
print("Testing errors:", errors.round(2))
print("Testing MAE:", round(mae, 2))


# 9. Predict score for new study hours
new_hours = np.array([[7]])

new_prediction = model.predict(new_hours)

print("\nPredicted score for 7 hours:", new_prediction[0])


# 10. Visualize actual and predicted values
plt.scatter(X_train, y_train, label="Training data")
plt.scatter(X_test, y_test, label="Actual test scores")

plt.plot(X, model.predict(X), label="Regression line")

plt.scatter(
    new_hours,
    new_prediction,
    color="red",
    label="New prediction"
)

plt.xlabel("Hours Studied")
plt.ylabel("Scores")
plt.title("Linear Regression - Actual vs Predicted Values")

plt.legend()
plt.show()
