import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

def preprocess_and_split(dataset):
    # in this case, there wont be pre-processino
    X = dataset.data[:, np.newaxis, 2]
    y = dataset.target
    # split the data
    X_train = X[:-20]
    X_test = X[-20:]
    y_train = y[:-20]
    y_test = y[-20:]
    return X_train, y_train, X_test, y_test

def execute_lineal_regression(X, y):
    # regression object
    regression = linear_model.LinearRegression()
    # training
    regression.fit(X, y)
    # prediction
    prediction = regression.predict(X_test)
    return regression, prediction

if __name__ == '__main__':
    diabetes = datasets.load_diabetes()

    X_train, y_train, X_test, y_test = preprocess_and_split(dataset = diabetes)

    regression, y_pred = execute_lineal_regression(X=X_train, y=y_train)

    # plotting
    print('Coeficients: \n', regression.coef_)  # [ 938.23786125]
    print("Mean squared error: \n %.2f" % mean_squared_error(y_test, y_pred))  # 2548.07
    print('Variance Score: \n %.2f' % r2_score(y_test, y_pred))  # 0.47

    plt.scatter(X_test, y_test, color='b', label='Data values')
    plt.plot(X_test, y_pred, color='r', label='Predict values')
    plt.title('Linear Regression Diabetest Sklearn data set')
    plt.legend()

    # plt.savefig("Linear_Regression_Diabetest_Sklearn_data_set.png")
    plt.show()