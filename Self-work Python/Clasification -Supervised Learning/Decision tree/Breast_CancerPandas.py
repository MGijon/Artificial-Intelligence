from sklearn.datasets import load_breast_cancer
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

bc = load_breast_cancer()
df = pd.DataFrame(bc.data, bc.feature_names) # NO FUNCIONA NI A TIROS!!
