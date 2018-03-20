import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

diabetes = datasets.load_diabetes()

X = diabetes.data[:, np.newaxis, 2]
X_train = X[:-20]
X_test = X[-20:]
y_train = diabetes.target[:-20]
y_test = diabetes.target[-20:]

# regression object
regression = linear_model.LinearRegression()

# training
regression.fit(X_train, y_train)

# prediction
y_pred = regression.predict(X_test)

# plotting
print('Coeficients: \n', regression.coef_)                                  # [ 938.23786125]

print("Mean squared error: \n %.2f" % mean_squared_error(y_test, y_pred))   # 2548.07

print('Variance Score: \n %.2f' %r2_score(y_test, y_pred))                  # 0.47


plt.scatter(X_test, y_test, color = 'b', label = 'Data values')
plt.plot(X_test, y_pred, color = 'r', label = 'Predict values')
plt.title('Linear Regression Diabetest Sklearn data set')
plt.legend()

#plt.savefig("Linear_Regression_Diabetest_Sklearn_data_set.png")
plt.show()
