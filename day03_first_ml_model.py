from sklearn.linear_model import LinearRegression

hours = [[1], [2], [3], [4]]
scores = [20, 40, 60, 80]

model=LinearRegression()
model.fit(hours,scores)

prediction=model.predict([[6]])
print("predicted score for 5 hours of study:",prediction[0])

print("Learned coefficient:", model.coef_[0])
print("Learned intercept:", model.intercept_)

print("Predictions for training data:", model.predict(hours))
print("Actual scores:", scores)