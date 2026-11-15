import numpy as np
import matplotlib.pyplot as plt

# Student dataset
X = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 30, 40, 50])

# Initialize model parameters
m = 0
c = 0

# Learning rate
learning_rate = 0.01

# Number of iterations
iterations = 1000

# Prediction function
def predict(X, m, c):
    return m * X + c


# Cost function (Mean Squared Error)
def calculate_cost(y, predictions):
    return np.mean((y - predictions) ** 2)

# Gradient Descent
for i in range(iterations):

    # Make predictions
    predictions = predict(X, m, c)

    # Calculate gradients
    dm = (-2 / len(X)) * np.sum(X * (y - predictions))
    dc = (-2 / len(X)) * np.sum(y - predictions)

    # Update model parameters
    m = m - learning_rate * dm
    c = c - learning_rate * dc

    # Display cost every 100 iterations
    if i % 100 == 0:
        cost = calculate_cost(y, predict(X, m, c))
        print("Iteration:", i, "Cost:", cost)

        # Display final results
print("\nTraining Completed!")

print("Final Slope:", m)
print("Final Intercept:", c)

# Predict marks for a student studying 7 hours
new_hours = 7
predicted_marks = predict(new_hours, m, c)

print("Predicted Marks for 7 hours:", predicted_marks)

# Final cost
final_predictions = predict(X, m, c)
final_cost = calculate_cost(y, final_predictions)
print("Final MSE:", final_cost)

# Visualize the trained model
plt.scatter(X, y, label="Actual Data")

plt.plot(X, predict(X, m, c), color="red", label="Predicted Line")

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Student Performance - Gradient Descent")

plt.legend()
plt.show()