from sklearn import datasets
import numpy as np
import matplotlib as plt

diabetes = datasets.load_diabetes()

X = diabetes.data
y = diabetes.target

print(X.shape)          # (442, 10)
print(y.shape)          # (442,)


print("we can print for instane the ? of the first 50 samples:\n")
#print(len([X[i, 0] for i in range (50)]))        # 50 elements
print([X[i, 0] for i in range (50)])




'''


https://github.com/scikit-learn/scikit-learn/blob/f3320a6f/sklearn/datasets/base.py#L552


def load_diabetes(return_X_y=False):
    """Load and return the diabetes dataset (regression).
    ==============      ==================
    Samples total       442
    Dimensionality      10
    Features            real, -.2 < x < .2
    Targets             integer 25 - 346
    ==============      ==================
    Read more in the :ref:`User Guide <datasets>`.
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
        'data', the data to learn and 'target', the regression target for each
        sample.
    (data, target) : tuple if ``return_X_y`` is True
        .. versionadded:: 0.18
    """

    module_path = dirname(__file__)
    base_dir = join(module_path, 'data')
    data = np.loadtxt(join(base_dir, 'diabetes_data.csv.gz'))
    target = np.loadtxt(join(base_dir, 'diabetes_target.csv.gz'))

    with open(join(module_path, 'descr', 'diabetes.rst')) as rst_file:
        fdescr = rst_file.read()

    if return_X_y:
        return data, target

    return Bunch(data=data, target=target, DESCR=fdescr,
                 feature_names=['age', 'sex', 'bmi', 'bp',
                                's1', 's2', 's3', 's4', 's5', 's6'])


'''