from sklearn import datasets 
import numpy as np 

iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
Y = iris.target

#print(np.unique(Y))       -> [0 1 2] = Iris-Setosa, Iris-Versicolor, and Iris-Virginica
#--------------------------------------------------------------------------------------------

from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.3, random_state = 0)

#--------------------------------------------------------------------------------------------

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

#--------------------------------------------------------------------------------------------

from sklearn.linear_model import Perceptron

ppn = Perceptron(n_iter = 40, eta0 = 0.1, random_state = 0)
ppn.fit(X_train_std, y_train)

y_pred = ppn.predict(X_test_std)
print('Misclassified Samples: %d' %(y_test != y_pred).sum())

#--------------------------------------------------------------------------------------------

'''
DeprecationWarning: This module was deprecated in version 0.18 in favor of the model_selection
module into which all the refactored classes and functions are moved. Also note that the
interface of the new CV iterators are different from that of this module. This module will be removed in 0.20.
"This module will be removed in 0.20.", DeprecationWarning)
'''