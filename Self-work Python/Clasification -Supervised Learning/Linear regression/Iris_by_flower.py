'''
    Regression models for each caracteristic (sepal and petal size) or each flower, not a
    classification problem.
'''
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
features
# print(X[:, :2]) # two first features: sepal length (cm) and sepal width (cm)

## ===== ##
## SEPAL ##
## ===== ##

Sepal = X[:, :2]
Sepal_length = Sepal[:, 0]
Sepal_width = Sepal[:, 1]

plt.figure(figsize = (10, 7.5))
plt.scatter(Sepal_length[:50], Sepal_width[:50], label = 'Setosa')
plt.scatter(Sepal_length[50:100], Sepal_width[50:100], label = 'Versicolor')
plt.scatter(Sepal_length[100:], Sepal_width[100:], label = 'Virginica')
plt.legend()
plt.xlabel('Sepal length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.show()

# just selecting Setosa and Versicolor species

SL_Setosa = Sepal_length[:50]
SL_Versicolor = Sepal_length[50:100]
SW_Setosa = Sepal_width[:50]
SW_Versicolor = Sepal_width[50:100]

plt.figure(figsize = (10, 7.5))
plt.scatter(SL_Setosa, SW_Setosa, label = 'Setosa')
plt.scatter(SL_Versicolor, SW_Versicolor, label = 'Versicolor')
plt.legend()
plt.xlabel('Sepal length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.show()

## LINEAR REGRESSION
## =================

# Petal length and width
X = iris.data[:, :2]
X = X[:100]
X_train = X[:40]
X_train
len(X_train)
np.insert(X_train, X[50:90])
len(X_train)


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
