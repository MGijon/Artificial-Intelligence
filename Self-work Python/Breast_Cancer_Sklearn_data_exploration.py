from sklearn import datasets
import numpy as np
import matplotlib as plt

## information about the data : https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)
##                            : http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html#sklearn.datasets.load_breast_cancer
##  =========================================================================================================================================================

# load and inspect the dataset:
bc = datasets.load_breast_cancer()
X = bc.data
y = bc.target

#print(type(bc))             # <class 'sklearn.datasets.base.Bunch'>

#print(bc.DESCR)             # Show the description of the data

#print(np.unique(y))         # [0 1]
#print(bc.target_names)      # ['malignant' 'benign']

#print(bc.feature_names)     # ['mean radius' 'mean texture' 'mean perimeter' 'mean area'
                            #  'mean smoothness' 'mean compactness' 'mean concavity'
                            #  'mean concave points' 'mean symmetry' 'mean fractal dimension'
                            #  'radius error' 'texture error' 'perimeter error' 'area error'
                            #  'smoothness error' 'compactness error' 'concavity error'
                            #  'concave points error' 'symmetry error' 'fractal dimension error'
                            #  'worst radius' 'worst texture' 'worst perimeter' 'worst area'
                            #  'worst smoothness' 'worst compactness' 'worst concavity'
                            #  'worst concave points' 'worst symmetry' 'worst fractal dimension']

'''
print(type(bc.feature_names))       # <class 'numpy.ndarray'>
print(bc.feature_names.data)        # <memory at 0x10d852f48>
print(bc.feature_names.dtype)       # <U23
print(bc.feature_names.strides)     # (92,)
print(bc.feature_names.shape)       # (30,)
print(len(bc.feature_names))        # 30
'''

print(type(X))              # <class 'numpy.ndarray'>
print(X.data)               # <memory at 0x108dfaf48>
print(X.dtype)              # float64
print(X.strides)            # (240, 8)
print(X.shape)              # (569, 30)
print(len(X))               # 569
'''
print(type(y))              # <class 'numpy.ndarray'>
print(y.data)               # <memory at 0x11092ef48>
print(y.dtype)              # int64
print(y.strides)            # (8,)
print(y.shape)              # (569,)
print(len(y))               # 569
'''

#print(bc.feature_names[1])  # mean texture
# Print the data corresponds with the data 'mean texture':
#print(X[:, 1])
# it has (number of samples)
#print(len(X[:,1]))          # 569
#print(np.corrcoef(X[:,0], X[:,1])) # between 'mean texture' and 'mean radius' there is a 0.32378189 coef correlation of Pearsons






'''

https://github.com/scikit-learn/scikit-learn/blob/b661a9c8/sklearn/datasets/base.py#L390


def load_breast_cancer(return_X_y=False):

    """Load and return the breast cancer wisconsin dataset (classification).
    The breast cancer dataset is a classic and very easy binary classification
    dataset.
    =================   ==============
    Classes                          2
    Samples per class    212(M),357(B)
    Samples total                  569
    Dimensionality                  30
    Features            real, positive
    =================   ==============
    Parameters
    ----------
    return_X_y : boolean, default=False
        If True, returns ``(data, target)`` instead of a Bunch object.
        See below for more information about the `data` and `target` object.
        .. versionadded:: 0.18
    Returns
    -------
    data : Bunch
        Dictionary-like object, the interesting attributes are:
        'data', the data to learn, 'target', the classification labels,
        'target_names', the meaning of the labels, 'feature_names', the
        meaning of the features, and 'DESCR', the
        full description of the dataset.
    (data, target) : tuple if ``return_X_y`` is True
        .. versionadded:: 0.18
    The copy of UCI ML Breast Cancer Wisconsin (Diagnostic) dataset is
    downloaded from:
    https://goo.gl/U2Uwz2
    Examples
    --------
    Let's say you are interested in the samples 10, 50, and 85, and want to
    know their class name.
    >>> from sklearn.datasets import load_breast_cancer
    >>> data = load_breast_cancer()
    >>> data.target[[10, 50, 85]]
    array([0, 1, 0])
    >>> list(data.target_names)
    ['malignant', 'benign']
    """
    module_path = dirname(__file__)
    data, target, target_names = load_data(module_path, 'breast_cancer.csv')

    with open(join(module_path, 'descr', 'breast_cancer.rst')) as rst_file:
        fdescr = rst_file.read()

    feature_names = np.array(['mean radius', 'mean texture',
                              'mean perimeter', 'mean area',
                              'mean smoothness', 'mean compactness',
                              'mean concavity', 'mean concave points',
                              'mean symmetry', 'mean fractal dimension',
                              'radius error', 'texture error',
                              'perimeter error', 'area error',
                              'smoothness error', 'compactness error',
                              'concavity error', 'concave points error',
                              'symmetry error', 'fractal dimension error',
                              'worst radius', 'worst texture',
                              'worst perimeter', 'worst area',
                              'worst smoothness', 'worst compactness',
                              'worst concavity', 'worst concave points',
                              'worst symmetry', 'worst fractal dimension'])

    if return_X_y:
        return data, target

    return Bunch(data=data, target=target,
                 target_names=target_names,
                 DESCR=fdescr,
                 feature_names=feature_names)


'''