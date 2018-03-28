import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

bh = datasets.load_boston()

features = bh.feature_names
X = bh.data
Y = bh.target

#X_train = Xsjdoa
#X_test = zd
'''
X = diabetes.data[:, np.newaxis, 2]
X_train = X[:-20]
X_test = X[-20:]
y_train = diabetes.target[:-20]
y_test = diabetes.target[-20:]
'''

regression = linear_model.LinearRegression()
regresion.fix(X_train, Y_train)
y_pred = regression.predict(X_test)
