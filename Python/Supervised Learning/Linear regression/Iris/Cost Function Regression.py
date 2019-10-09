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

#print(flowers) # ['setosa' 'versicolor' 'virginica']
#print(features) # ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

sepal_length_Setosa = X[:, 0][:50]
sepal_width_Setosa= X[:, 1][:50]

sepal_length_Versicolor = X[:, 0][50:100]
sepal_width_Versicolor= X[:, 1][50:100]

sepal_length_Virginica = X[:, 0][100:150]
sepal_width_Virginica = X[:, 1][100:150]

#print(np.corrcoef(sepal_length_Setosa, sepal_width_Setosa)) # 0.74678037
#print(np.corrcoef(sepal_length_Versicolor, sepal_width_Versicolor)) # 0.52591072
#print(np.corrcoef(sepal_length_Virginica, sepal_width_Virginica)) # 0.45722782

## Let's try to predict the value of Sepal Lenght for the Setosa with the data of Sepal Width (Setosa)
## and study the efect of the Learning Rate on the Gradient Descent Algorithem for the Linear Regression.
## ------------------------------------------------------------------------------------------------------

Y = sepal_length_Setosa
X = sepal_width_Setosa

batch = 500
alpha = 0.01 # Learning Rate

theta0 = 0 # Intercept
theta1 = 0.5 # Slope

parameters = [] # (iteration, theta0, theta1)

for iteration in range(0, batch):
	parameters.append((iteration, theta0, theta1))
	
	summatory0 = 0
	summatory1 = 0

	for observation in range(0, len(X)):
		summatory0 += (theta0 + theta1*X[observation]) - Y[observation]
		summatory1 += ((theta0 + theta1*X[observation]) - Y[observation] )* X[observation]

	theta0 = theta0 - alpha * (1 / len(X)) * summatory0
	theta1 = theta1 - alpha * (1 / len(X)) * summatory1


iterations = [x for x in range(0, batch)]
data_theta0 = [x[1] for x in parameters]
data_theta1 = [x[2] for x in parameters]

#plt.figure(figsize=(20, 14))
plt.plot(iterations, data_theta0, label="Intercept")
plt.plot(iterations, data_theta1, label="Slop")
plt.title("Gradient Descent algorithm for Linear Regression")
plt.xlabel("Number of iterations")
plt.legend()
#plt.savefig("Images/GDConvergence")
plt.show()


## Let's print the Cost Function
## -----------------------------


def cost_function(theta0, theta1, m=len(X)):
	constant = 1 / (2 * m) 
	cost = 0
	for observation in range(0, len(X)):
			cost += np.power((theta0 + theta1*X[observation]) - Y[observation], 2)

	return cost*constant


cost_function_values = []

for i in range(batch):
	cost_function_values.append(cost_function(data_theta0[i], data_theta1[i]))

#plt.figure(figsize=(20, 14))
plt.plot(iterations, cost_function_values)
plt.title("Cost Funcion evolution applying GD for Linear Regression")
plt.xlabel("Number of iterations")
plt.legend()
#plt.savefig("Images/Cost Function")
plt.show()


