from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt

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


print("Print the 25th first values of the 'mean radius' variable:\n")
print([X[i, 0] for i in range(25)])

X_mean_radius_100 = [X[i, 0] for i in range(100)]
X_mean_perimeter_100 = [X[i, 2] for i in range(100)]

y_100 = y[0:100]

# print(len(y_100))     # 100

X_mean_radius_100_sick = [X_mean_radius_100[i] for i in range(100) if y_100[i] == 0]
X_mean_radius_100_OK = [X_mean_radius_100[i] for i in range(100) if y_100[i] == 1]

X_mean_perimeter_100_sick = [X_mean_perimeter_100[i] for i in range(100) if y_100[i] == 0]
X_mean_perimeter_100_OK = [X_mean_perimeter_100[i] for i in range(100) if y_100[i] == 1]

plt.scatter(X_mean_radius_100_sick, X_mean_perimeter_100_sick, color = 'red', label = 'sick')
plt.scatter(X_mean_radius_100_OK, X_mean_perimeter_100_OK, color = 'green', label = 'ok')
plt.xlabel('Radius')
plt.ylabel('Perimeter')
plt.title('Breast Cancer data set exploration 1')
plt.legend() # add the 'label' attirbutes to the picture
plt.savefig('Breast Cancer data set exploration 1.png')
plt.show()

## ------------------------
## Now for all the data set:
## ========================

X_mean_radius_sick = [X[i, 0] for i in range(len(y)) if y[i] == 0]
X_mean_radius_OK = [X[i, 0] for i in range(len(y)) if y[i] == 1]

X_mean_perimeter_sick = [X[i, 2] for i in range(len(y)) if y[i] == 0]
X_mean_perimeter_OK = [X[i, 2] for i in range(len(y)) if y[i] == 1]

plt.scatter(X_mean_radius_OK, X_mean_perimeter_OK, color = 'green', label = 'ok')
plt.scatter(X_mean_radius_sick , X_mean_perimeter_sick, color = 'red', label = 'sick')

plt.xlabel('Radius')
plt.ylabel('Perimeter')
plt.title('Breast Cancer data set exploration 2')
plt.legend() # add the 'label' attirbutes to the picture
plt.savefig('Breast Cancer data set exploration 2.png')
plt.show()

# ------------------------
## Now for all the data set and mean area:
## ========================

X_mean_area_sick = [X[i, 3] for i in range(len(y)) if y[i] == 0]
X_mean_area_OK = [X[i, 3] for i in range(len(y)) if y[i] == 1]

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(X_mean_radius_OK, X_mean_perimeter_OK, X_mean_area_OK, color = 'green', label = 'ok')
ax.scatter(X_mean_radius_sick, X_mean_perimeter_sick, X_mean_area_sick, color = 'red', label = 'sick')
ax.set_xlabel('Radius')
ax.set_ylabel('Perimeter')
ax.set_zlabel('Area')
plt.title('Breast Cancer data set exploration 3')
plt.legend() # add the 'label' attirbutes to the picture
plt.savefig('Breast Cancer data set exploration 3.png')
plt.show()


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