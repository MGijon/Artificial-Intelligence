from sklearn import tree
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()
clf = tree.DecisionTreeRegressor()
clf = clf.fit(diabetes.data, diabetes.target)

clf.predict(diabetes.data[:1, :])

clf.predict(diabetes.data[:3, :])

clf.predict(diabetes.data[:5, :])
