"""Gradient Descent Optimization."""
import numpy as np

def hypotesis(X, theta):
    """Compute the value of the Hypotesis Function in the Linear Regression.
            h(theta) = theta^{T} X = theta_0 + theta_1 * x_1
    """

    h = theta[0] * X[0] + theta[1] * X[1]
    return h

def almostCostFunction(X, y, m, theta):
    """Compute the coeficients for the Gradient Descent algorithm than involves in
       some form the Cost Function.
    """
    total = [0, 0]

    for row in range(0, m):
        total[0] += (hypotesis(X[row], theta) - y[row]) * X[row][0]
        total[1] += (hypotesis(X[row], theta) - y[row]) * X[row][1]

    total[0] = total[0] / m
    total[1] = total[1] / m

    return total

def gradienDescent(X, y, m, theta, iterations, alpha):
    """Optimize the Cost Function for the Linear Regression using Gradient Descent."""

    # Gradient Descent
    for iteration in range(iterations):
        almostCost_0, almostCost_1 =  almostCostFunction(X, y, m, theta)
        newtheta0 = theta[0] - alpha * almostCost_0
        newtheta1 = theta[1] - alpha * almostCost_1
        # update
        theta[0] = newtheta0
        theta[1] = newtheta1

    return theta
