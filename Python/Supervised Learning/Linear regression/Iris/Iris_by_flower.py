'''
    Regression models for each caracteristic (sepal and petal size) or each flower.
'''

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import os

iris = datasets.load_iris()

X = iris.data
Y = iris.target

flowers = iris.target_names
features = iris.feature_names
# print(X[:, :2]) # two first features: sepal length (cm) and sepal width (cm)

## ===== ##
## SEPAL ##
## ===== ##

Sepal = X[:, :2]
Sepal_length = Sepal[:, 0]
Sepal_width = Sepal[:, 1]

SL_Setosa = Sepal_length[:50]
SL_Versicolor = Sepal_length[50:100]
SL_Virginica = Sepal_length[100:]
SW_Setosa = Sepal_width[:50]
SW_Versicolor = Sepal_width[50:100]
SW_Virginica = Sepal_width[100:]

plt.figure(figsize = (10, 7.5))
plt.scatter(SL_Setosa, SW_Setosa, label = 'Setosa')
plt.scatter(SL_Versicolor, SW_Versicolor, label = 'Versicolor')
plt.scatter(SL_Virginica, SW_Virginica, label = 'Virginica')
plt.legend()
plt.xlabel('Sepal length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Iris: Sepal size')
#plt.savefig('Images/Iris sepal size')
plt.show()

# ------ #
# Setosa #
# ------ #

SL_Setosa_train = SL_Setosa[:40, np.newaxis] # 80% of the samples
SW_Setosa_train = SW_Setosa[:40]
SL_Setosa_test = SL_Setosa[40:, np.newaxis]
SW_Setosa_test = SW_Setosa[40:]
# SL_Setosa_train.shape (40, 1) : [n_samples, n_features]

regression = linear_model.LinearRegression()
regression.fit(SL_Setosa_train, SW_Setosa_train)
prediction = regression.predict(SL_Setosa_test)

print('Coeficients: \n', regression.coef_)
print("Mean squared error: \n %.2f" % mean_squared_error(SW_Setosa_test, prediction))
print('Variance Score: \n %.2f' %r2_score(SW_Setosa_test, prediction))

plt.scatter(SL_Setosa_test, SW_Setosa_test, color = 'b', label = 'Data values')
plt.plot(SL_Setosa_test, prediction, color = 'r', label = 'Predict values')
plt.title('')
plt.legend()
plt.title('Sepal Setosa size regression')
#plt.savefig('Images/Sepal Setosa regression')
plt.show()

# ---------- #
# Versicolor #
# ---------- #

SL_Versicolor_train = SL_Versicolor[:40, np.newaxis] # 80% of the n_samples
SW_Versicolor_train = SW_Versicolor[:40]
SL_Versicolor_test = SL_Versicolor[40:, np.newaxis]
SW_Versicolor_test = SW_Versicolor[40:]

regression = linear_model.LinearRegression()
regression.fit(SL_Versicolor_train, SW_Versicolor_train)
prediction = regression.predict(SL_Versicolor_test)

print('Coeficients: \n', regression.coef_)
print("Mean squared error: \n %.2f" % mean_squared_error(SW_Versicolor_test, prediction))
print('Variance Score: \n %.2f' %r2_score(SW_Versicolor_test, prediction))

plt.scatter(SL_Versicolor_test, SW_Versicolor_test, color = 'b', label = 'Data values')
plt.plot(SL_Versicolor_test, prediction, color = 'r', label = 'Predict values')
plt.title('')
plt.legend()
plt.title('Sepal Versicolor size regression')
#plt.savefig('Images/Sepal Versicolor regression')
plt.show()


# --------- #
# Virginica #
# --------- #

SL_Virginica_train = SL_Virginica[:40, np.newaxis] # 80% of the n_samples
SW_Virginica_train = SW_Virginica[:40]
SL_Virginica_test = SL_Virginica[40:, np.newaxis]
SW_Virginica_test = SW_Virginica[40:]

regression = linear_model.LinearRegression()
regression.fit(SL_Virginica_train, SW_Virginica_train)
prediction = regression.predict(SL_Virginica_test)

print('Coeficients: \n', regression.coef_)
print("Mean squared error: \n %.2f" % mean_squared_error(SW_Virginica_test, prediction))
print('Variance Score: \n %.2f' %r2_score(SW_Virginica_test, prediction))

plt.scatter(SL_Virginica_test, SW_Virginica_test, color = 'b', label = 'Data values')
plt.plot(SL_Virginica_test, prediction, color = 'r', label = 'Predict values')
plt.title('')
plt.legend()
plt.title('Sepal Virginica size regression')
#plt.savefig('Images/Sepal Virginica regression')
plt.show()


################################################################################
################################################################################

## ===== ##
## PETAL ##
## ===== ##

Petal = X[:, 2:]
Petal_length = Petal[:, 0]
Petal_width = Petal[:, 1]

PL_Setosa = Petal_length[:50]
PL_Versicolor = Petal_length[50:100]
PL_Virginica = Petal_length[100:]
PW_Setosa = Petal_width[:50]
PW_Versicolor = Petal_width[50:100]
PW_Virginica = Petal_width[100:]

plt.figure(figsize = (10, 7.5))
plt.scatter(PL_Setosa, PW_Setosa, label = 'Setosa')
plt.scatter(PL_Versicolor, PW_Versicolor, label = 'Versicolor')
plt.scatter(PL_Virginica, PW_Virginica, label = 'Virginica')
plt.legend()
plt.xlabel('Petal length (cm)')
plt.ylabel('Petal Width (cm)')
plt.title('Iris: Petal size')
#plt.savefig('Images/Iris petal size')
plt.show()


# ------ #
# Setosa #
# ------ #

PL_Setosa_train = PL_Setosa[:40, np.newaxis]
PL_Setosa_test = PL_Setosa[40:, np.newaxis]
PW_Setosa_train = PW_Setosa[:40]
PW_Setosa_test = PW_Setosa[40:]
len(PL_Setosa_train)
len(PL_Setosa_test)
regression = linear_model.LinearRegression()
regression.fit(PL_Setosa_train, PW_Setosa_train)
prediction = regression.predict(PL_Setosa_test)

print('Coeficients: \n', regression.coef_)
print("Mean squared error: \n %.2f" % mean_squared_error(PW_Setosa_test, prediction))
print('Variance Score: \n %.2f' %r2_score(PW_Setosa_test, prediction))

plt.scatter(PL_Setosa_test, PW_Setosa_test, color = 'b', label = 'Data values')
plt.plot(PL_Setosa_test, prediction, color = 'r', label = 'Predict values')
plt.legend()
plt.title('Petal Setosa size regression')
#plt.savefig('Images/Petal Setosa regression')
plt.show()

# ---------- #
# Versicolor #
# ---------- #

PL_Versicolor_train = PL_Versicolor[:40, np.newaxis]
PL_Versicolor_test = PL_Versicolor[40:, np.newaxis]
PW_Versicolor_train = PW_Versicolor[:40]
PW_Versicolor_test = PW_Versicolor[40:]

regression = linear_model.LinearRegression()
regression.fit(PL_Versicolor_train, PW_Versicolor_train)
prediction = regression.predict(PL_Versicolor_test)

print('Coeficients: \n', regression.coef_)
print("Mean squared error: \n %.2f" % mean_squared_error(SW_Versicolor_test, prediction))
print('Variance Score: \n %.2f' %r2_score(SW_Versicolor_test, prediction))

plt.scatter(PL_Versicolor_test, PW_Versicolor_test, color = 'b', label = 'Data values')
plt.plot(PL_Versicolor_test, prediction, color = 'r', label = 'Predict values')
plt.legend()
plt.title('Petal Versicolor size regression')
#plt.savefig('Images/Petal Versicolor regression')
plt.show()

# --------- #
# Virginica #
# --------- #

PL_Virginica_train = PL_Virginica[:40, np.newaxis]
PL_Virginica_test = PL_Virginica[40:, np.newaxis]
PW_Virginica_train = PW_Virginica[:40]
PW_Virginica_test = PW_Virginica[40:]

regression = linear_model.LinearRegression()
regression.fit(PL_Virginica_train, PW_Virginica_train)
prediction = regression.predict(PL_Virginica_test)

print('Coeficients: \n', regression.coef_)
print("Mean squared error: \n %.2f" % mean_squared_error(PW_Virginica_test, prediction))
print('Variance Score: \n %.2f' %r2_score(PW_Virginica_test, prediction))

plt.scatter(PL_Virginica_test, PW_Virginica_test, color = 'b', label = 'Data values')
plt.plot(PL_Virginica_test, prediction, color = 'r', label = 'Predict values')
plt.legend()
plt.title('Petal Virginica size regression')
#plt.savefig('ImagesPetal Virginica regression')
plt.show()
