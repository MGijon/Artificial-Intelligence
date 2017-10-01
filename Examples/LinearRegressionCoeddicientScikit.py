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

print('Slope: %.3f' % slr.coef_[0])							# Slope: 9.102
print('Intercept: %.3f' % slr.intercept_)					# Intercept: -34.671