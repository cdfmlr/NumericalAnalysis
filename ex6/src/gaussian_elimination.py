import numpy as np


def gaussian_elimination_sequence(a, b):
    """
    用「顺序高斯消去法」解线性方程 `ax = b`。

    Args:
        a : np_array_like 系数矩阵（nxn）
        b : np_array_like 右端常数（n）

    Returns:
        x : np.array `ax=b` 的解（n）

    Raises:
        Exception("求解失败") if a[k][k] == 0
    """
    A = np.c_[a, b]  # 增广矩阵

    n, c = A.shape
    assert c == n + 1, f'bad shape: {A.shape}'

    x = np.zeros(n)

    # 消元
    for k in range(n-1):
        if A[k][k] == 0:
            raise Exception("求解失败")

        for i in range(k+1, n):
            m = A[i][k] / A[k][k]
            A[i][k] = 0
            for j in range(k+1, n+1):
                A[i][j] -= A[k][j] * m

    # 回代
    x[n-1] = A[n-1][n] / A[n-1][n-1]
    for k in range(n-2, -1, -1):  # from n-2 (included) to 0 (included)
        for j in range(k+1, n):
            A[k][n] -= A[k][j] * x[j]
        x[k] = A[k][n] / A[k][k]

    return x


def gaussian_elimination(a, b, sequence=False):
    """
    用「列主元高斯消去法」解线性方程 `ax = b`。

    本函数可以通过「列主元高斯消元法」或「顺序高斯消元法」计算，
    通过参数 sequence 控制，默认 sequence=False 使用「列主元高斯消元法」。

    Args:
        a : np_array_like 系数矩阵（nxn）
        b : np_array_like 右端常数（n）

    Returns:
        x : np.array `ax=b` 的解（n）

    Raises:
        Exception("求解失败") if a[k][k] == 0
    """
    A = np.c_[a, b]  # 增广矩阵

    n, c = A.shape
    assert c == n + 1, f'bad shape: {A.shape}'

    x = np.zeros(n)

    # 消元
    for k in range(0, n-1):
        if not sequence:  # 列主元
            i_max = k + np.argmax(np.abs(A[k:n, k]))

            if A[i_max][k] == 0:
                raise Exception("A 奇异，求解失败")

            A[[i_max, k]] = A[[k, i_max]]  # swap rows

        for i in range(k+1, n):
            m = A[i][k] / A[k][k]
            for j in range(k+1, n+1):
                A[i][j] -= A[k][j] * m

    # 回代
    if a[n-1][n-1] == 0:
        raise Exception("矩阵奇异，求解失败")

    x[n-1] = A[n-1][n] / A[n-1][n-1]
    for i in range(n-2, -1, -1):  # from n-2 (included) to 0 (included)
        for j in range(i+1, n):
            A[i][n] -= A[i][j] * x[j]
        x[i] = A[i][n] / A[i][i]

    return x
