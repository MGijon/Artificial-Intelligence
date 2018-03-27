import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

iris = datasets.load_iris()

X = iris.data
Y = iris.target

flowers = iris.target_names
features = iris.feature_names
flowers
print(X[:, :2]) # two first features: sepal length (cm) and sepal width (cm)

Sepal = X[:, :2]
Sepal_length = Sepal[:, 0]
Sepal_width = Sepal[:, 1]

plt.figure(figsize = (10, 7.5))
plt.scatter(Sepal_length[:50], Sepal_width[:50], label = 'Setosa')
plt.scatter(Sepal_length[50:100], Sepal_width[50:100], label = 'Versicolor')
plt.scatter(Sepal_length[100:], Sepal_width[100:], label = 'Virginica')
plt.legend()
plt.xlabel('Sepal length')
plt.ylabel('Sepal Width')
plt.show()

# we select just the Setosa and Versicolor flowers by now

SL_Setosa = Sepal_length[:50]
SL_Versicolor = Sepal_length[50:100]
SW_Setosa = Sepal_width[:50]
SW_Versicolor = Sepal_width[50:100]

plt.figure(figsize = (10, 7.5))
plt.scatter(SL_Setosa, SW_Setosa, label = 'Setosa')
plt.scatter(SL_Versicolor, SW_Versicolor, label = 'Versicolor')
plt.legend()
plt.xlabel('Sepal length')
plt.ylabel('Sepal Width')
plt.show()

################################################################################
'''
# now we define the train and the test sets

X_train = Sepal[:75] # 75% of the samples
X_test = Sepal[75:100]

Y_train = iris.target[:75]
Y_test = iris.target[75:100]

# regression object
regression = linear_model.LinearRegression()
# training
regression.fit(X_train, Y_train)
# prediction
y_pred = regression.predict(X_test)

# plotting
print('Coeficients: \n', regression.coef_)

print("Mean squared error: \n %.2f" % mean_squared_error(Y_test, y_pred))

print('Variance Score: \n %.2f' %r2_score(Y_test, y_pred))
'''

X = iris.data[:, np.newaxis, 2]
X = X[:50]
X.shape
X_train = X[:-20]
X_test = X[-20:]
Y = iris.target[:50]
y_train = Y[:-20]
y_test = Y[-20:]
# creo que el problema es que he de limitar antes los datos con los que trabajo
# regression object
regression = linear_model.LinearRegression()
len(X)
# training
regression.fit(X_train, y_train)

# prediction
y_pred = regression.predict(X_test)

# plotting
print('Coeficients: \n', regression.coef_)                                  # [ 938.23786125]

print("Mean squared error: \n %.2f" % mean_squared_error(y_test, y_pred))   # 2548.07

print('Variance Score: \n %.2f' %r2_score(y_test, y_pred))                  # 0.47


#plt.scatter(X_test, y_test, label = 'Data values')
plt.scatter(SL_Setosa, SW_Setosa, label = 'Setosa')
plt.plot(X_test, y_pred, color = 'r', label = 'Predict values')
plt.title('')
plt.legend()
plt.show()


################################################################################
diabetes = datasets.load_diabetes()

X = diabetes.data[:, np.newaxis, 2]
X_train = X[:-20]
X_test = X[-20:]
y_train = diabetes.target[:-20]
y_test = diabetes.target[-20:]

regression = linear_model.LinearRegression()

regression.fit(X_train, y_train)

y_pred = regression.predict(X_test)

print('Coeficients: \n', regression.coef_)                                  # [ 938.23786125]
print("Mean squared error: \n %.2f" % mean_squared_error(y_test, y_pred))   # 2548.07
print('Variance Score: \n %.2f' %r2_score(y_test, y_pred))                  # 0.47

plt.scatter(X_test, y_test, color = 'b', label = 'Data values')
plt.plot(X_test, y_pred, color = 'r', label = 'Predict values')
plt.title('Linear Regression Diabetest Sklearn data set')
plt.legend()
plt.show()
