from sklearn import datasets
import numpy as np
import matplotlib as plt

bh = datasets.load_boston()

X = bh.data
y = bh.target

print(bh.feature_names)     # ['CRIM' 'ZN' 'INDUS' 'CHAS' 'NOX' 'RM' 'AGE' 'DIS' 'RAD' 'TAX' 'PTRATIO' 'B' 'LSTAT']

#print(bh.DESCR)             # data set description

import seaborn as sns

sns.set(style = 'whitegrid', context = 'notebook')

columns = ['CRIM', 'AGE', 'PTRATIO']

## CRIM :     per capita crime rate by town
## AGE :      proportion of owner-occupied units built prior to 1940
## PTRATIO :  pupil-teacher ratio by town

CRIM = X[:, 0]
AGE = X[:, 6]
PTRATIO = X[:, 10]

print(type(CRIM))           # <class 'numpy.ndarray'>
















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
