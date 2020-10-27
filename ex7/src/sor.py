import numpy as np


def sor(A, b, x0=None, w=1, eps=1e-5, max_steps=5000, verbose=False):
    """逐次超松驰法（Successive over-relaxation, SOR）求解线性方程组:
        A @ x = b

    Args:
        A:  np_array_like, 系数矩阵
        b:  np_array_like, 右端常数
        x0: np_array_like, 迭代初值
            default x0=None means using random values.
        w:  float, 松弛因子 w > 0
            default w=1，即 Gauss–Seidel 迭代
        eps: float, 精度要求
        max_steps: int, 最大迭代次数
        verbose: bool, 如果计算成功，打印出结果及迭代次数

    Returns:
        x: 方程组的解

    Raises:
        ValueError: w 小于等于 0
        ValueError: A 和 b 形状不符合要求
        Expection:  达到最大迭代次数，仍不满足精度
    """
    if w <= 0:
        raise ValueError(f"unexpected w = {w} < 0")

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

    _inv_DsWL = np.linalg.pinv(D - w * L)

    B = _inv_DsWL @ ((1-w) * D + w * U)
    f = w * _inv_DsWL @ b

    x = x0
    i = 0

    for i in range(int(max_steps)):
        x_prev = np.array(x)  # deep copy

        x = B @ x + f

        if np.all(np.abs(x - x_prev) <= eps):  # 达到精度要求
            break
    else:
        raise Exception(
            f"cannot reach eps ({eps}) after max_steps ({max_steps}). The last result: x = {x}")

    if verbose:
        print(f"sor (w={w}) get result x = {x} after {i} iterations.")

    return x
