import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

x = np.array([1, 2, 3, 4, 5, 6])

y = np.array([1, 4, 9, 16, 25, 36])

X_train = x[:4].reshape(-1, 1)
y_train = y[:4]

X_test = x[4:].reshape(-1, 1)
y_test = y[4:]

print("Training inputs:", X_train.flatten())
print("Training answers:", y_train)

print("Testing inputs:", X_test.flatten())
print("Testing answers:", y_test)

model = LinearRegression()

model.fit(X_train, y_train)

train_predictions = model.predict(X_train)
train_mse = mean_squared_error(y_train, train_predictions)

print("Training MSE:", round(train_mse, 2))

predictions = model.predict(X_test)
print("Test predictions:", predictions.round(2))
print("Correct test answers:", y_test)

print("Actual values:", y)
print("Predicted values:", predictions.round(2))

mse = mean_squared_error(y_test, predictions)
print("Test Mean Squared Error:", round(mse, 2))

new_x = np.array([[7]])
new_prediction=model.predict(new_x)
print("prediction for x=7 :",round(new_prediction[0],2))

print("Number of training examples:", X_train.shape[0])
print("Number of features:", X_train.shape[1])