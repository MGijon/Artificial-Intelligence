"""Prediction of values for Simple Linear Regression."""

def predict(x, theta):
    """y_hat = theta_0 + theta_1 * x."""

    return theta[0] + theta[1] * x
