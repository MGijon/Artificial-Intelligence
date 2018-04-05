from sklearn.datasets import load_breast_cancer
from sklearn import tree

bc = load_breast_cancer()

clf = tree.DecisionTreeClassifier()
clf = clf.fit(bc.data, bc.target)

clf.predict(bc.data[:50, :])
clf.predict_proba(bc.data[:50, :])

# Changing the maximun max_depth:
clf = tree.DecisionTreeClassifier(max_depth = 4)
clf = clf.fit(bc.data, bc.target)

clf.predict(bc.data[:50, :])
clf.predict_proba(bc.data[:50, :])

# Now I'll train the model with less data
clf = tree.DecisionTreeClassifier()
clf = clf.fit(bc.data[:50, :], bc.target[:50])

clf.predict(bc.data[50:, :])
clf.predict_proba(bc.data[50:, :])
predictions = clf.predict(bc.data[50:, :])

wrongs = 0
j = 50
for i in predictions:
    if bc.target[j] != i:
        wrongs += 1
    j += 1
wrongs
# 99 bad predictions
