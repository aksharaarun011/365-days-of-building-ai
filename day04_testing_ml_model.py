from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

hours = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
scores = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]

X_train,X_test,y_train,y_test= train_test_split(
    hours,scores,test_size=0.2,random_state=42
)

print("training size=",len(X_train))
print("test size=",len(X_test))

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print("Predicted scores:", predictions)

print("Actual scores:", y_test)
print("Prediction errors:", predictions - y_test)

mae = mean_absolute_error(y_test, predictions)
print("Mean Absolute Error (MAE):", mae)
