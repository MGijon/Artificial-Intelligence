''' RANdom SAmple Consensus (RANSAC)
	
	It's a regression model algorithm which fits a regression model to a subset 
	of the data (called 'inliers')

	Algorithm:
	----------
	1.- Select a random number of samples to be inliers and fit the model.
	2.- Test all other data points against the fitted model and add those points that
		fall within a user-given tolerance to the inliers.
	3.- Refit the model using all inliers.
	4.- Estimate the erro of the fitted model versus the inliers.
	5.- Terminate the algorithm if the perfomance meets a certain user-defined
		threshold or if a fixed number of iterations has been reached; go back to 
		the step 1 otherwise.
'''

import pandas as pd
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data', header = None,  sep = '\s+')
df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
df.head()

import numpy as np 

X = df[['RM']].values
y = df['MEDV'].values

from sklearn.linear_model import LinearRegression

from sklearn.linear_model import RANSACRegressor

ransac = RANSACRegressor(LinearRegression(), max_trials = 100, min_samples = 50, residual_metric = lambda x: np.sum(np.abs(x), axis = 1), residual_threshold = 0.5, random_state = 0)

ransac.fit(X, y)

import matplotlib.pyplot as plt

inlier_mask = ransac.inlier_mask_

outlier_mask = np.logical_not(inlier_mask)

line_X = np.arange(3, 10, 1)
line_y_ransac = ransac.predict(line_X[:, np.newaxis])

plt.scatter(X[inlier_mask], y[inlier_mask], c = 'blue', marker = 'o', label = 'Inliers')
plt.scatter(X[outlier_mask], y[outlier_mask], c = 'lightgreen', marker = 's', label = 'Outliers')

plt.plot(line_X, line_y_ransac, color = 'red')

plt.xlabel('Average number of rooms [RM]')
plt.ylabel('Price in $1000\'s [MEDV]')
plt.legend(loc = 'upper left')

plt.show()
