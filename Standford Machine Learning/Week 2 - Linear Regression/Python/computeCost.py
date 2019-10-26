"""Description."""
import numpy as np

def hypotesis(X, theta):
    """Compute the value of the Hypotesis Function in the Linear Regression.
            h(theta) = theta^{T} X = theta_0 + theta_1 * x_1
    """
    h = theta[0] * X[0] + theta[1] * X[1]
    return h

def computeCost(X, y, m, theta):
    """Obtain the value of the Cost Function."""

    cost = 0
    for row in range(0, m):
        auxiliar = np.power(hypotesis(X[row], theta) - y[row], 2)
        cost += auxiliar

    cost = cost / (2 * m)


    return cost
