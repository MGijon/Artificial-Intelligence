from sklearn.datasets import load_diabetes
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

diabetes = load_diabetes()
feature_names = ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']
df = pd.DataFrame(diabetes.data, columns = feature_names)
y = diabetes.target

dtr = DecisionTreeRegressor()
dtr = dtr.fit(df, y)
