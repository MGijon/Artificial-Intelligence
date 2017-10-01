import pandas as pd 					# Python Data Analysis Library
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data', header = None,  sep = '\s+')
df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
df.head()

import matplotlib.pyplot as plt 
import seaborn as sns 					# seaborn: statistical data visualization package

sns.set(style = 'whitegrid', context = 'notebook')

cols = ['LSTAT', 'INDUS', 'NOX', 'RM', 'MEDV']
sns.pairplot(df[cols], size = 2.5)

plt.show()