from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()

clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

clf.predict(iris.data[:1, :])
clf.predict_proba(iris.data[:1, :])

clf.predict(iris.data[50:100, :])
clf.predict_proba(iris.data[50:100, :])
clf.predict(iris.data[100:, :])
clf.predict_proba(iris.data[100:, :])
