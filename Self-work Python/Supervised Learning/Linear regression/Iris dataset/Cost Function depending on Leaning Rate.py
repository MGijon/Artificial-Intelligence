import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets
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

## ------------------------------------------------
## GRADIENT DESCENT FOR LINEAR REGRESSION ALGORITHM
## ------------------------------------------------

Y = sepal_length_Setosa
X = sepal_width_Setosa
batch = 500

def GradientDescent(theta0, theta1, alpha):
	
	alpha = 0.01 # Learning Rate

	parameters = [] # (iteration, alpha, theta0, theta1)

	for iteration in range(0, batch):
		parameters.append((iteration, alpha, theta0, theta1))
		
		summatory0 = 0
		summatory1 = 0

		for observation in range(0, len(X)):
			summatory0 += (theta0 + theta1*X[observation]) - Y[observation]
			summatory1 += ((theta0 + theta1*X[observation]) - Y[observation] )* X[observation]

		theta0 = theta0 - alpha * (1 / len(X)) * summatory0
		theta1 = theta1 - alpha * (1 / len(X)) * summatory1

	return parameters

super_parameters = []

alpha_values = [1, 0.1, 0.01, 0.001]

for x in alpha_values:
	super_parameters.append(GradientDescent(theta0=0, theta1=1, alpha=x))

def cost_function(theta0, theta1, m=len(X)):
	constant = 1 / (2 * m) 
	cost = 0
	for observation in range(0, len(X)):
			cost += np.power((theta0 + theta1*X[observation]) - Y[observation], 2)


	return cost*constant



iterations = [x for x in range(0, batch)]

for alpha in alpha_values:
	parameters = GradientDescent(theta0=0, theta1=1, alpha=x)
	data_theta0 = [x[2] for x in parameters]
	data_theta1 = [x[3] for x in parameters]
	cost_function_values = []
	for i in range(batch):
		cost_function_values.append(cost_function(data_theta0[i], data_theta1[i]))

	plt.figure(figsize=(10, 7))
	plt.plot(iterations, cost_function_values)
	plt.title("Cost Funcion evolution applying GD for Linear Regression, Learning Rate " + str(alpha))
	plt.xlabel("Number of iterations")
	plt.legend()
	plt.savefig("Images/Cost Function - Learning Rate - " + str(alpha) + ".png")
	plt.show()


