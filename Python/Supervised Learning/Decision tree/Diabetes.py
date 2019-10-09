from sklearn import tree
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()
clf = tree.DecisionTreeRegressor()
clf = clf.fit(diabetes.data, diabetes.target)

clf.predict(diabetes.data[:1, :])

clf.predict(diabetes.data[:3, :])

clf.predict(diabetes.data[:5, :])

################################################################################
# Now I'll train the model with less data
clf = tree.DecisionTreeClassifier()
clf = clf.fit(diabetes.data[:50, :], diabetes.target[:50])

predictions = clf.predict(diabetes.data[50:, :])

wrongs = 0
j = 0
for i in predictions:
    if diabetes.target[j] != i:
        wrongs += 1
    j += 1
wrongs

# 388 bad predictions!!
