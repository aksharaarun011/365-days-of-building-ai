from sklearn.linear_model import LinearRegression

hours = [[1], [2], [3], [4], [5]]
scores = [20, 40, 60, 80, 100]

model = LinearRegression()
model.fit(hours, scores)
print("Model training complete!")

prediction= model.predict([[6]])
print("Predicted score for 6 hours of study:", round(prediction[0], 2))

new_hours = [[6], [7], [8]]
new_predictions = model.predict(new_hours)
print("New study hours:", new_hours)
print("Predicted scores:", new_predictions)

user_hours= float(input("enter hours of study:"))
user_prediction= model.predict([[user_hours]])
print("predicted score:", round(user_prediction[0],2))