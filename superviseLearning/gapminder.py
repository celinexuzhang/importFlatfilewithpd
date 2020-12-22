#instruction-
#Import numpy and pandas as their standard aliases.
#Read the file 'gapminder.csv' into a DataFrame df using the read_csv() function.
#Create array X for the 'fertility' feature and array y for the 'life' target variable.
#Reshape the arrays by using the .reshape() method and passing in -1 and 1.

#Answer
# Import numpy and pandas
import numpy as np
import pandas as pd

# Read the CSV file into a DataFrame: df
df = pd.read_csv('C:/Users/celin/OneDrive/Desktop/Learning/python/machinelearningwithpython/superviselearning/gapminder.csv')

# Create arrays for features and target variable
y = df['life'].values
X = df['fertility'].values

# Print the dimensions of X and y before reshaping
print("Dimensions of y before reshaping: {}".format(y.shape))
print("Dimensions of X before reshaping: {}".format(X.shape))

# Reshape X and y
y = y.reshape(-1, 1)
X = X.reshape(-1, 1)

# Print the dimensions of X and y after reshaping
print("Dimensions of y after reshaping: {}".format(y.shape))
print("Dimensions of X after reshaping: {}".format(X.shape))

#In this exercise, you will split the Gapminder dataset into training and testing sets, and then fit and predict a linear regression over all features. In addition to computing the R2 score, you will also compute the Root Mean Squared Error (RMSE), which is another commonly used metric to evaluate regression models. The feature array X and target variable array y have been pre-loaded for you from the DataFrame df.
#instruction
#Import LinearRegression from sklearn.linear_model, mean_squared_error from sklearn.metrics, and train_test_split from sklearn.model_selection.
#Using X and y, create training and test sets such that 30% is used for testing and 70% for training. Use a random state of 42.
#Create a linear regression regressor called reg_all, fit it to the training set, and evaluate it on the test set.
#Compute and print the R2 score using the .score() method on the test set.
#Compute and print the RMSE. To do this, first compute the Mean Squared Error using the mean_squared_error() function with the arguments y_test and y_pred, and then take its square root using np.sqrt().

# Import necessary modules
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=42)

# Create the regressor: reg_all
reg_all = LinearRegression()

# Fit the regressor to the training data
reg_all.fit(X_train, y_train)

# Predict on the test data: y_pred
y_pred = reg_all.predict(X_test)

# Compute and print R^2 and RMSE
print("R^2: {}".format(reg_all.score(X_test, y_test)))
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print("Root Mean Squared Error: {}".format(rmse))

#5fold cross validation
#Import LinearRegression from sklearn.linear_model and cross_val_score from sklearn.model_selection.
#Create a linear regression regressor called reg.
#Use the cross_val_score() function to perform 5-fold cross-validation on X and y.
#Compute and print the average cross-validation score. You can use NumPy's mean() function to compute the average.

# Import the necessary modules
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

# Create a linear regression object: reg
reg = LinearRegression()

# Compute 5-fold cross-validation scores: cv_scores
cv_scores = cross_val_score(reg, X, y, cv=5)

# Print the 5-fold cross-validation scores
print(cv_scores)

# Print the average 5-fold cross-validation score
print("Average 5-Fold CV Score: {}".format(np.mean(cv_scores)))

#K-fold CV comparison
#Import LinearRegression from sklearn.linear_model and cross_val_score from sklearn.model_selection.
#Create a linear regression regressor called reg.
#Perform 3-fold CV and then 10-fold CV. Compare the resulting mean scores.

# Import necessary modules
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

# Create a linear regression object: reg
reg = LinearRegression()

# Perform 3-fold CV
cvscores_3 = cross_val_score(reg, X, y, cv = 3)
print(np.mean(cvscores_3))

# Perform 10-fold CV
cvscores_10 = cross_val_score(reg, X, y, cv = 10)
print(np.mean(cvscores_10))

#regularization I: Lasso
#Import Lasso from sklearn.linear_model.
#Instantiate a Lasso regressor with an alpha of 0.4 and specify normalize=True.
#Fit the regressor to the data and compute the coefficients using the coef_ attribute.
#Plot the coefficients on the y-axis and column names on the x-axis. This has been done for you, so hit 'Submit Answer' to view the plot!

# Import Lasso
from sklearn.linear_model import Lasso
import matplotlib.pyplot as plt

# Instantiate a lasso regressor: lasso
lasso = Lasso(alpha=0.4, normalize=True)

# Fit the regressor to the data
lasso.fit(X, y)

# Compute and print the coefficients
lasso_coef = lasso.coef_googl
print(lasso_coef)

# Plot the coefficients
plt.plot(range(len(df_columns)), lasso_coef)
plt.xticks(range(len(df_columns)), df_columns.values, rotation=60)
plt.margins(0.02)
plt.show()
