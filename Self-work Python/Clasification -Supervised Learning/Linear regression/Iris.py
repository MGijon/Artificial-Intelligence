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

# now we define the train and the test sets
