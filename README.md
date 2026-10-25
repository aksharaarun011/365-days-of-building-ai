# 365 Days of Building AI

Welcome to my 365 Days of Building AI challenge!

## About This Challenge
I am learning Python, Artificial Intelligence, and Generative AI by building projects every day.


## Day 1: Hello AI
- Created my first Python program.
- Learned how to use the `print()` function.
- Ran a Python file from the terminal.
- Practiced Git and GitHub basics.
- Uploaded my code to GitHub.

## Technologies
- Python
- Git
- GitHub
- VS Code

## Goal
Build my programming skills step by step and develop a portfolio of AI projects over 365 days.

**Day 1 completed! 🚀**

# Day 2: MiniBot — My First Chatbot

## Project Overview
MiniBot is a simple rule-based chatbot built using Python. It responds to user messages by checking them against predefined rules.

## Concepts Learned
- Strings and text input
- `if`, `elif`, and `else` conditions
- Comparing strings using `==`
- Using `.strip()` to remove extra spaces
- Using `.lower()` to normalize text
- `while` loops to repeat conversations
- `break` to stop the loop

## Features
- Responds to greetings
- Answers "How are you?"
- Responds to "What is your name?"
- Responds to "Thank you"
- Stops when the user types `bye`
- Handles uppercase and extra spaces in messages

## How to Run
1. Install Python 3.
2. Open a terminal in the project folder.
3. Run:

   `python day02_first_chatbot.py`

## What I Learned
I learned how to use Python conditions and loops to create an interactive chatbot. I also learned that a rule-based chatbot follows predefined rules rather than learning patterns from a training dataset.

## Next Steps
- Add more responses.
- Improve how unknown messages are handled.
- Explore machine learning and build a model that learns from data.

## Day 3: My First Machine Learning Model

**Project:** Study-Hours Score Predictor

### What I built
- Created my first machine-learning model using Python and scikit-learn.
- Used Linear Regression to learn a pattern from example data.
- Trained the model using study hours and corresponding practice scores.
- Predicted a score for a new input.
- Inspected the learned coefficient and intercept.
- Compared predictions with the training data.

### What I learned
- The difference between rule-based programming and machine learning.
- Training data, model fitting, and predictions.
- Linear regression and the equation `y = wx + b`.
- Coefficients and intercepts.
- How to use scikit-learn in Python.
- Git commits, rebasing, and pushing code to GitHub.

### Project file
- `day03_first_ml_model.py`

**Status:** Completed ✅

**Note:** This project uses a small, invented dataset for learning. Its predictions are a demonstration and are not reliable estimates of real exam scores.


## Day 4: Testing and Evaluating a Machine Learning Model

**Project:** Evaluate a Linear Regression Model

### What I built
- Split a dataset into training and testing sets using `train_test_split`.
- Trained a Linear Regression model using only the training data.
- Predicted scores for unseen test examples.
- Compared predictions with actual target values.
- Calculated Mean Absolute Error (MAE) using scikit-learn.

### What I learned
- The difference between training data and test data.
- Why test data should be kept separate during training.
- How prediction errors are calculated.
- How MAE summarizes the average absolute prediction error.
- Why a small test set and artificial data do not prove real-world performance.

### Project file
- `day04_testing_ml_model.py`

**Status:** Completed ✅

## Day 5: Making Predictions with Machine Learning

**Project:** Predicting Values with Linear Regression

### What I built
- Trained a Linear Regression model using scikit-learn.
- Made predictions for individual and multiple inputs.
- Accepted user input with Python's `input()` and `float()`.
- Rounded predictions for cleaner output.

### What I learned
- How a trained model predicts values for new inputs.
- The difference between training a model and using it for prediction.
- Why scikit-learn expects input features in a 2D structure.
- How to use `round()` to format floating-point predictions.
- How to debug a machine learning input-shape error.

### Project file
- `day05_making_predictions.py`

**Note:** The dataset uses artificial values for learning and does not reliably predict real exam scores.

**Status:** Completed ✅

## Day 6: Underfitting and Overfitting

### What I learned
- Understood the difference between underfitting and overfitting.
- Used NumPy to prepare input features for a machine learning model.
- Trained a Linear Regression model using scikit-learn.
- Split data into training and testing sets.
- Evaluated predictions using Mean Squared Error (MSE).
- Compared training error with test error.
- Learned why testing on unseen data is important.

### Project
Created `day06_underfitting_overfitting.py` to explore how a simple linear regression model performs when predicting squared values.

### Experiment results
- Training examples: 4
- Number of features: 1
- Training MSE: 1.0
- Test MSE: 73.0

The model underfits the squared pattern because it uses only the original input feature `x` rather than `x²`.

### Key takeaway
A model should be evaluated on unseen data, not just the data it was trained on. Training performance alone does not guarantee good predictions on new examples.

