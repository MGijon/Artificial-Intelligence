from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt

bh = datasets.load_boston()

X = bh.data
y = bh.target

print(bh.feature_names)     # ['CRIM' 'ZN' 'INDUS' 'CHAS' 'NOX' 'RM' 'AGE' 'DIS' 'RAD' 'TAX' 'PTRATIO' 'B' 'LSTAT']

#print(bh.DESCR)             # data set description

columnas = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']


print(type(y))   # <class 'numpy.ndarray'>
print(y.shape)   # (506,)
print(X.shape)   #( 506, 13)

# Prices histogram
plt.hist(y, 50)
plt.title('Boston Houses Prices')
plt.ylabel('Prices')
plt.xlabel('')
plt.savefig('Boston_house_prices_data_exploration_1.png')
plt.show()

# Scatterplot Crim/Age/Dis vs. prices
plt.scatter(X[:, 0], y, c = 'b', label = 'Crime', marker = '^')
plt.scatter(X[:, 6], y, c = 'r', label = 'Age', marker = 'o')
plt.scatter(X[:, 7], y, c = 'g', label = 'Dis', marker  = (5, 1))
plt.legend()
plt.title('Prices against some variables')
plt.xlabel('Variables')
plt.ylabel('Prices')
plt.savefig('Boston_house_prices_data_exploration_2.png')
plt.show()

# looking for correlation between crime and the others variables:
Correlations =  [np.corrcoef(X[:, 0], X[:, i])[0, 1] for i in range(1,X.shape[1])]

print(np.where(Correlations == max(Correlations)))   # (array([7]),)

print(Correlations[7])                               # 0.62202890894

# now looking for the correlations between every pair of variables:
Correlations_matrix = np.ndarray((X.shape[1], X.shape[1])) # create a two dimensional array for every coeficient
for i in range(X.shape[1]):
    for j in range(X.shape[1]):
        Correlations_matrix[i, j] = np.corrcoef(X[:, i], X[:, j])[0, 1]

print(Correlations_matrix)

# eliminate the 1's from the diagonal
for i in range(X.shape[1])_
    Correlations_matrix[i, i] = 0

# look for the maximun value:
# tengo que usar reshape y buscar los valores, o puedo directamente??
'''


https://github.com/scikit-learn/scikit-learn/blob/b661a9c8/sklearn/datasets/base.py#L652


def load_boston(return_X_y=False):
    """Load and return the boston house-prices dataset (regression).
    ==============     ==============
    Samples total                 506
    Dimensionality                 13
    Features           real, positive
    Targets             real 5. - 50.
    ==============     ==============
    Parameters
    ----------
    return_X_y : boolean, default=False.
        If True, returns ``(data, target)`` instead of a Bunch object.
        See below for more information about the `data` and `target` object.
        .. versionadded:: 0.18
    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are:
        'data', the data to learn, 'target', the regression targets,
        and 'DESCR', the full description of the dataset.
    (data, target) : tuple if ``return_X_y`` is True
        .. versionadded:: 0.18
    Examples
    --------
    >>> from sklearn.datasets import load_boston
    >>> boston = load_boston()
    >>> print(boston.data.shape)
    (506, 13)
    """
    module_path = dirname(__file__)

    fdescr_name = join(module_path, 'descr', 'boston_house_prices.rst')
    with open(fdescr_name) as f:
        descr_text = f.read()

    data_file_name = join(module_path, 'data', 'boston_house_prices.csv')
    with open(data_file_name) as f:
        data_file = csv.reader(f)
        temp = next(data_file)
        n_samples = int(temp[0])
        n_features = int(temp[1])
        data = np.empty((n_samples, n_features))
        target = np.empty((n_samples,))
        temp = next(data_file)  # names of features
        feature_names = np.array(temp)

        for i, d in enumerate(data_file):
            data[i] = np.asarray(d[:-1], dtype=np.float64)
            target[i] = np.asarray(d[-1], dtype=np.float64)

    if return_X_y:
        return data, target

    return Bunch(data=data,
                 target=target,
                 # last column is target value
                 feature_names=feature_names[:-1],
                 DESCR=descr_text)


'''
