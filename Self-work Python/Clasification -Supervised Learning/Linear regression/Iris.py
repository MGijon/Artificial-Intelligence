import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

iris = datasets.load_iris()

X = iris.data
Y = iris.target

flowers = iris.target_names
features = iris.feature_names
