# General libraries
import os
import numpy as np

# Other functions
from warmUpExercise import *
from plotData import *
from computeCost import *
from gradientDescent import *
from predic import *

## ======== Part 1: Basic Function ======== ##
# Complete warmUpExercise
print('Runing warmUpExercise...\n')
print('5x5 Identity Matrix: \n')
print(warmUpExercise())
print('\n')

## ======== Part 2: Plotting ======== ##

f = open('../Data/ex1data1.txt')
content = f.readlines()
f.close()
X = []
y = []
m = len(content)
for line in content:
    line = line.replace('\n', '')
    x_, y_ = line.split(',')
    X.append(float(x_))
    y.append(float(y_))

plotData(x=X, y=y)

## ======== Part 3: Cost and Gradient Descent ======== ##

X1 = [[1, X[i]] for i in range(len(X))] # Add a column of 1's to X
theta = [0, 0]

# Some Gradient Descent settings
iterations = 1500
alpha = .01

print('Testing the cost function... \n')

initial_cost = computeCost(X=X1,
                           y=y,
                           m=m,
                           theta=theta)

print('The initial cost (before Gradient Descent optimization) = ', initial_cost)
print('The expected value (approx) 32.07\n')

another_test = computeCost(X=X1, y=y, m=m, theta=[-1, 2])
print('With theta_0 = -1 and theta_1 = 2 the cost value is ', another_test)
print('The expected value (approx) 54.24\n')

print('Runing Gradient Descent... \n')
thetaGD = gradienDescent(X=X1,
                         y=y,
                         m=m,
                         theta=theta,
                         iterations=iterations,
                         alpha=alpha)
print('Theta values = ', thetaGD)
print('Expected theta values (approx) = [-3.6303, 1.1664]\n')

plotRegresionLine(x=X, y=y, theta=thetaGD)

predic1 = predict(x=3500, theta=thetaGD)
predic2 = predict(x=7500, theta=thetaGD)

print('For population of 3500, we predict a profit of ', predic1)
print('For population of 7500, we predict a profit of ', predic2)


## ======== Part 4: Visualizing J(theta_0, theta_1) ======== ##

print('Visualizing J(theta_0, theta_1)... \n')

constant = 100
theta_0_vals = np.linspace(start=-10, stop=10, num=constant)
theta_1_vals = np.linspace(start=-10, stop=10, num=constant)

J = np.zeros((constant, constant))

for i in range(0, len(theta_0_vals)):
    for j in range(0, len(theta_1_vals)):
        theta_temporal = [theta_0_vals[i], theta_1_vals[j]]
        J[i][j] = computeCost(X=X1,
                              y=y,
                              m=m,
                              theta=theta_temporal)

plotJ(x=theta_0_vals, y=theta_1_vals, z=J)



## Estoy ya muy cansado de esta mierda y quierp irme a casa a mastu****
## quiero irme a casa de una maldita vez
