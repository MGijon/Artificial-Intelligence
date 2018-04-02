from sklearn import tree

'''
Takes as input two arrays: an array X, sparse or dense, of size [n_samples, n_features]
holding the training samples, and an array Y of integer values, size [n_samples],
holding the class labels for the training samples:
'''
X = [[0, 0], [1, 1]]
Y = [0, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

'''
After being fitted, the model can then be used to predict the class of samples:
'''

clf.predict([[2., 2.]])

'''
Alternatively, the probability of each class can be predicted, which is the fraction
of training samples of the same class in a leaf:
'''

clf.predict_proba([[2., 2.]])
