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

SL_Setosa = Sepal_length[:50]
SL_Versicolor = Sepal_length[50:100]
SL_Virginica = Sepal_length[100:]
SW_Setosa = Sepal_width[:50]
SW_Versicolor = Sepal_width[50:100]
SW_Viginica = Sepal_width[100:]

plt.figure(figsize = (10, 7.5))
plt.scatter(SL_Setosa, SW_Setosa, label = 'Setosa')
plt.scatter(SL_Versicolor, SW_Versicolor, label = 'Versicolor')
plt.scatter(SL_Virginica, SW_Viginica, label = 'Virginica')
plt.legend()
plt.xlabel('Sepal length (cm)')
plt.ylabel('Sepal Width (cm)')
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
PW_Viginica = Petal_width[100:]

plt.figure(figsize = (10, 7.5))
plt.scatter(PL_Setosa, PW_Setosa, label = 'Setosa')
plt.scatter(PL_Versicolor, PW_Versicolor, label = 'Versicolor')
plt.scatter(PL_Virginica, PW_Viginica, label = 'Virginica')
plt.legend()
plt.xlabel('Petal length (cm)')
plt.ylabel('Petal Width (cm)')
plt.show()
