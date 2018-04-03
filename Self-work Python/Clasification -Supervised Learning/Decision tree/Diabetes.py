from sklearn import tree
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(diabetes.data, diabetes.target)## NO FUNCIONA Y NO SÉ POR QUÉ

clf.predict(diabetes.data[:1, :])
clf.predict_proba(diabetes.data[:1, :])
clf.predict(diabetes.data[:3, :])
clf.predict_proba(diabetes.data[:3, :])

clf.predict(diabetes.data[:5, :])
clf.predict_proba(diabetes.data[:5, :]) # no me fío de los resultados, demasiado raros
