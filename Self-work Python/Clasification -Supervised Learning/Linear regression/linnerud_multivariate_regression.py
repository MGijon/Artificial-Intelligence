import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from mpl_toolkits.mplot3d import Axes3D


lin = datasets.load_linnerud()

lin_features = lin.feature_names

X = lin.data[:, np.newaxis, 2]
X_train = X[:-15]
X_test = X[-15:]
y_train = lin.target[:-15]
y_test = lin.target[-15:]

regression = linear_model.LinearRegression()

# training
regression.fit(X_train, y_train)

# prediction
y_pred = regression.predict(X_test)

# plotting
print('Coeficients: \n', regression.coef_)                                  # [ 938.23786125]

print("Mean squared error: \n %.2f" % mean_squared_error(y_test, y_pred))   # 2548.07

print('Variance Score: \n %.2f' %r2_score(y_test, y_pred))

'''
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_test[:,0], X_test[:,1], X_test[:,2])
plt.scatter(X_test, y_test, color = 'b', label = 'Data values')
plt.plot(X_test, y_pred, color = 'r', label = 'Predict values')
plt.title('Linear Regression Diabetest Sklearn data set')
plt.legend()

plt.show()
'''
