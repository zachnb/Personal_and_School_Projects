# -*- coding: utf-8 -*-
"""model_building.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17sj0nurxcfEZBUTiByahXyx2nPwz-PRP
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# LR1: Dataset: kc_house_data.csv

# Load the dataset
kc_data = pd.read_csv('/content/sample_data/kc_house_data.csv')

# Defining the feature (X) and target variable (y)
X = kc_data['sqft_living'].values.reshape(-1, 1)  # Input: Square footage of houses
y = kc_data['price'].values  # Output: Price of houses

# Splitting the dataset into the Training set and Test set (80% train, 20% test)
# Here, we're dividing the data into two parts: one to train our model and one to test its performance.
# This allows us to check how well our model can predict data after training.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Model building and linear regression process
# We're creating a Linear Regression model and fitting it to our training data.
# This means finding the line that best fits the relationship between square footage and price.
model = LinearRegression()
model.fit(X_train, y_train)

# Model Results
# Here we're printing the intercept and coefficient of our regression model.
# These values help us understand the equation of the line our model has determined.
print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_[0])

# Model Accuracy
# We're calculating the R-squared value, which is a measure of how well our model
# fits the data. It ranges from 0 to 1, with 1 indicating a perfect fit.
# A higher R-squared value means our model has more variance in the data.
y_pred = model.predict(X_test)
print("R-squared:", metrics.r2_score(y_test, y_pred))

# Visualizations

# Before running the linear regression:
# (1) A scatterplot of the raw data, x vs y
# This plot shows the relationship between square footage and price before our
# regression model is applied. Each point represents a house, with square footage
# on the x-axis and price on the y-axis.
plt.scatter(X, y, color='blue', edgecolor='black')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Regression Line')
plt.title('Raw Data: Square Footage vs Price')
plt.xlabel('Square Footage')
plt.ylabel('Price')
plt.ticklabel_format(axis="both", style="plain") # Adjust to avoid scientific notation
plt.show()

# After running the linear regression:
# (2) Plot actual vs predicted values
# This plot compares the actual price of houses to the price predicted by our model.
# Ideally, all points should fall on the diagonal line, indicating perfect predictions.
plt.scatter(y_test, y_pred, color='blue', edgecolor='black', label='Actual')
plt.plot(y_test, y_test, color='red', linewidth=2)  # Plotting predicted values as a line
plt.title('Actual vs Predicted Values')
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.ticklabel_format(axis="both", style="plain") # Adjust to avoid scientific notation
plt.show()

# (3) Plot the error
# This plot shows the difference between the actual price and the price predicted by our model.
# Ideally, these differences should be evenly distributed around 0, indicating unbiased predictions.
plt.scatter(y_pred, y_test - y_pred, color='green', edgecolor='black')
plt.title('Error Plot')
plt.xlabel('Predicted')
plt.ylabel('Residuals')
plt.axhline(y=0, color='black', linewidth=1)
plt.show()

# LR2: Dataset: student_scores.csv

# Load the dataset
student_scores = pd.read_csv('/content/sample_data/student_scores.csv')

# Defining the feature (X) and target variable (y)
X = student_scores['Hours'].values.reshape(-1, 1)  # Input: Hours studied by students
y = student_scores['Scores'].values  # Output: Scores achieved by students

# Splitting the dataset into the Training set and Test set (80% train, 20% test)
# Splitting the data into two parts: one for training the model and one for testing
# its performance.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Model building and linear regression process
# Creating a Linear Regression model and fitting it to our training data.
model = LinearRegression()
model.fit(X_train, y_train)

# Model Results
# Printing the intercept and coefficient of our linear regression model.
print("\nIntercept:", model.intercept_)
print("Coefficient:", model.coef_[0])

# Model Accuracy
# Calculating the R-squared value, a measure of how well our model fits the data.
y_pred = model.predict(X_test)
print("R-squared:", metrics.r2_score(y_test, y_pred))

# Visualizations

# Before running the linear regression:
# (1) A scatterplot of the raw data, x vs y
# This plot shows the relationship between hours studied and scores achieved before
# regression is applied.
plt.scatter(X, y, color='blue', edgecolor='black')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Regression Line')
plt.title('Raw Data: Hours vs Scores')
plt.xlabel('Hours Studied')
plt.ylabel('Scores')
plt.ticklabel_format(axis="both", style="plain")  # Adjust to avoid scientific notation
plt.show()

# After running the linear regression:
# (2) Plot actual vs predicted values
# This plot compares the actual scores achieved to the scores predicted by
# the regression model.
plt.scatter(y_test, y_pred, color='blue', edgecolor='black', label='Actual vs Predicted')
plt.plot(y_test, y_test, color='red', linewidth=2)  # Plotting the diagonal line
plt.title('Actual vs Predicted Values')
plt.xlabel('Actual Score')
plt.ylabel('Predicted Score')
plt.ticklabel_format(axis="both", style="plain") # Adjust to avoid scientific notation
plt.show()

# (3) Plot the error
# This plot shows the difference between the actual score and the score predicted
# by the regression model.
plt.scatter(y_pred, y_test - y_pred, color='green', edgecolor='black')
plt.title('Error Plot')
plt.xlabel('Predicted')
plt.ylabel('Residuals')
plt.axhline(y=0, color='black', linewidth=1)
plt.ticklabel_format(axis="both", style="plain")  # Adjust to avoid scientific notation
plt.show()
