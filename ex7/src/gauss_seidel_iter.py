import numpy as np


def gauss_seidel_iter(A, b, x0=None, eps=1e-5, max_steps=5000, verbose=False):
    """高斯-赛德尔迭代（Gauss–Seidel method）求解线性方程组:
        A @ x = b

    Args:
        A:  np_array_like, 系数矩阵
        b:  np_array_like, 右端常数
        x0: np_array_like, 迭代初值
            default x0=None means using random values.
        eps: float, 精度要求
        max_steps: int, 最大迭代次数
        verbose: bool, 如果计算成功，打印出结果及迭代次数

    Returns:
        x: 方程组的解

    Raises:
        ValueError: A 和 b 形状不符合要求
        Expection:  达到最大迭代次数，仍不满足精度
    """
    A = np.array(A)
    b = np.array(b)

    n, m = A.shape
    if n != m or n != len(b):
        raise ValueError(f"Not match: A({n, m}) and b({len(b)},)")

    if not x0:
        x0 = np.random.random(n)

    # A =  D - L - U

    D = np.diag(np.diag(A))
    L = - np.tril(A, -1)
    U = - np.triu(A, 1)

    inv_DsL = np.linalg.pinv(D - L)

    B = inv_DsL @ U
    f = inv_DsL @ b

    x = x0
    i = 0
    for i in range(int(max_steps)):
        x_prev = np.array(x)  # deep copy

        inv_DsL = np.linalg.pinv(D - L)
        x = B @ x + f

        if np.all(np.abs(x - x_prev) <= eps):  # 达到精度要求
            break
    else:
        raise Exception(
            f"cannot reach eps ({eps}) after max_steps ({max_steps}). The last result: x = {x}")

    if verbose:
        print(f"gauss_seidel_iter get result x = {x} after {i} iterations.")

    return x
