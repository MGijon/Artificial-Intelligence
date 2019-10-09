import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import os

iris = datasets.load_iris()

x = iris.data
y = iris.target

## Sepal length and width

Sepal = x[:, :2]

def Sepal_Scatter():
	plt.scatter(Sepal[:,0][:50], Sepal[:,1][:50], label="Setosa")
	plt.scatter(Sepal[:,0][50:100], Sepal[:,1][50:100], label="Virginica")
	plt.scatter(Sepal[:,0][100:], Sepal[:,1][100:], label="Versicolor")
	plt.legend()
	plt.title("Sepal length and width scatter plot")
	plt.xlabel("Length (cm)")
	plt.ylabel("Width (cm)")
	plt.savefig("Images/scatter_Sepal.png")
	plt.show()

Sepal_Scatter()


## in the future: aplication of the gradient descent algorithm to this problem