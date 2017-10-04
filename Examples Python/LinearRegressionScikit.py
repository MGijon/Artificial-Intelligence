import pandas as pd
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data', header = None,  sep = '\s+')
df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
df.head()

import numpy as np 

X = df[['RM']].values
y = df['MEDV'].values

from sklearn.linear_model import LinearRegression

slr = LinearRegression()
slr.fit(X, y)

import matplotlib.pyplot as plt

def lin_regplot(X, y, model):
	plt.scatter(X, y, c = 'blue')
	plt.plot(X, model.predict(X), color = 'red')
	return None
	
lin_regplot(X, y, slr)
plt.xlabel('Average number of rooms [RM] (standarized)')
plt.ylabel('Prices in $1000\'s [MEDV] (standarized)')

plt.show()
