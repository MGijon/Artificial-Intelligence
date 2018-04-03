from sklearn.datasets import load_iris
from sklearn import tree
import numpy as np
import random

iris = load_iris()

## splitter = 'best' (by default)
## ================

clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

clf.predict(iris.data[:50, :])
clf.predict_proba(iris.data[:50, :])

clf.predict(iris.data[50:100, :])
clf.predict_proba(iris.data[50:100, :])

clf.predict(iris.data[100:, :])
clf.predict_proba(iris.data[100:, :])

## splitter = 'random'
## ==================

clf_2 = tree.DecisionTreeClassifier(splitter = 'random')
clf_2 = clf_2.fit(iris.data, iris.target)

clf_2.predict(iris.data[:50, :])
clf_2.predict_proba(iris.data[:50, :])

clf_2.predict(iris.data[50:100, :])
clf_2.predict_proba(iris.data[50:100, :])

clf_2.predict(iris.data[100:, :])
clf_2.predict_proba(iris.data[100:, :])
