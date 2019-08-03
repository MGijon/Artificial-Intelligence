import sklearn.datasets as datasets
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns = iris.feature_names)
y = iris.target

dtc = DecisionTreeClassifier()
dtc = dtc.fit(df, y)
