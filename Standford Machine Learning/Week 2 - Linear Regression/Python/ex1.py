# General libraries
import os

# Other functions
from warmUpExercise import *
from plotData import *

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
