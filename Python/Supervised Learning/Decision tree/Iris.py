from sklearn.datasets import load_iris
from sklearn import tree
import numpy as np
import random

iris = load_iris()

## CRITERION:
## =========
## The function to measure the quality of a split.
## Supported criteria are “gini” for the Gini impurity and
## “entropy” for the information gain.

## (1) criterion = 'gini' (by default)
## -------------

clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

clf.predict(iris.data[:50, :])
clf.predict_proba(iris.data[:50, :])

clf.predict(iris.data[50:100, :])
clf.predict_proba(iris.data[50:100, :])

clf.predict(iris.data[100:, :])
clf.predict_proba(iris.data[100:, :])

## (2) criterion = 'entropy'
## -------------

clf_2 = tree.DecisionTreeClassifier(criterion = 'entropy')
clf_2 = clf_2.fit(iris.data, iris.target)

clf_2.predict(iris.data[:50, :])
clf_2.predict_proba(iris.data[:50, :])

clf_2.predict(iris.data[50:100, :])
clf_2.predict_proba(iris.data[50:100, :])

clf_2.predict(iris.data[100:, :])
clf_2.predict_proba(iris.data[100:, :])

## SPLITTER:
## ========
## The strategy used to choose the split at each node.
## Supported strategies are “best” to choose the best split and
## “random” to choose the best random split.

## (1) splitter = 'best' (by default)
## ------------

# done

## (2) splitter = 'random'
## ------------

clf_2 = tree.DecisionTreeClassifier(splitter = 'random')
clf_2 = clf_2.fit(iris.data, iris.target)

clf_2.predict(iris.data[:50, :])
clf_2.predict_proba(iris.data[:50, :])

clf_2.predict(iris.data[50:100, :])
clf_2.predict_proba(iris.data[50:100, :])

clf_2.predict(iris.data[100:, :])
clf_2.predict_proba(iris.data[100:, :])


## MAX_DEPTH:
## =========
## The maximum depth of the tree. If None, then nodes are expanded
## until all leaves are pure or until all leaves contain less than
## min_samples_split samples.

## (1) max_depth = 'None' (by default)
## -------------

# done

## (2) max_depth = int
## -------------

clf_2 = tree.DecisionTreeClassifier(max_depth = 2)
clf_2 = clf_2.fit(iris.data, iris.target)

clf_2.predict(iris.data[:50, :])
clf_2.predict_proba(iris.data[:50, :])

clf_2.predict(iris.data[50:100, :])
clf_2.predict_proba(iris.data[50:100, :])

clf_2.predict(iris.data[100:, :])
clf_2.predict_proba(iris.data[100:, :])


clf_3 = tree.DecisionTreeClassifier(max_depth = 4)
clf_3 = clf_3.fit(iris.data, iris.target)

clf_3.predict(iris.data[:50, :])
clf_3.predict_proba(iris.data[:50, :])

clf_3.predict(iris.data[50:100, :])
clf_3.predict_proba(iris.data[50:100, :])

clf_3.predict(iris.data[100:, :])
clf_3.predict_proba(iris.data[100:, :])

# There are more paramethers that i'll try in the future

# source : http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
