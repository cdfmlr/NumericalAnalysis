import numpy as np
from functools import reduce


def fit(X, y):
    """正规方程拟合

    Args:
        X: 
        y: 目标值 np.array([y0, y1, ...])
    """
    return np.dot(np.dot(np.linalg.pinv(np.dot(X.T, X)), X.T), y)
