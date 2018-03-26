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

plt.scatter(X_test[], Y_test, color = 'b', label = 'Data values')
plt.plot(X_test, y_pred, color = 'r', label = 'Predict values')
plt.title('Linear Regression Iris Sklearn data set')
plt.legend()

#plt.savefig("Linear_Regression_Diabetest_Sklearn_data_set.png")
plt.show()

# http://scikit-learn.org/stable/modules/linear_model.html
