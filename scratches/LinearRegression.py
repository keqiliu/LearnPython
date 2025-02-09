import random
import numpy as np
from sklearn.linear_model import LinearRegression

# define input
X_raw = np.array([1, 2, 3, 4, 5])
y_raw = np.array([1.5, 3.1, 4.9, 6.2, 7.8])

# write own function to get coefficient
X = np.matrix([np.ones(X_raw.shape), X_raw]).T
y = np.matrix(y_raw).T

# get analytical estimate of coefficients
beta = np.linalg.inv(X.T * X) * X.T * y

# y = ax + b
b = beta[0,0]
a = beta[1,0]

# Try get fitting error
y_fit = np.array([a*x+b for x in X_raw])
# Get R^2
# get residual sum of square
SS_res = sum([x*x for x in (y_fit - y_raw)])
# total sum of squares
y_raw_mean = np.average(y_raw)
SS_total = sum([x*x for x in (y_raw - y_raw_mean)])
R_square = 1 - SS_res/SS_total

# validate using sklearn
X = X_raw.reshape(len(X_raw),1)
y = y_raw.reshape(len(y_raw),1)
reg = LinearRegression().fit(X, y)

b1 = reg.intercept_[0]
print(f'b diff = {b1-b}')

a1 = reg.coef_[0,0]
print(f'a diff = {a1-a}')

y_fit1 = reg.predict(X).flatten()
print(f'y_fit diff = {y_fit1-y_fit}')

R_square1 = reg.score(X,y)
print(f'R^2 diff = {R_square1-R_square}')
