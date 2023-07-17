# Произвести вычисления как в пункте 2, но с вычислением intercept.
# Учесть, что изменение коэффициентов должно производиться на каждом шаге одновременно
# (то есть изменение одного коэффициента не должно влиять на изменение другого во время одной итерации).
import numpy as np

# Given data
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

# Define the learning rate and number of iterations
learning_rate = 0.0001
num_iterations = 1000

# Initialize the coefficients
slope = 0
intercept = 0

# Perform gradient descent
for _ in range(num_iterations):
    slope_gradient = (-2 / len(zp)) * np.sum(zp * (ks - (slope * zp + intercept)))
    intercept_gradient = (-2 / len(zp)) * np.sum(ks - (slope * zp + intercept))

    slope -= learning_rate * slope_gradient
    intercept -= learning_rate * intercept_gradient

linear_regression_coefficient = slope

print("Linear Regression Coefficient:", linear_regression_coefficient)
