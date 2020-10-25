import numpy as np


def lu(a, sequence=False, swap_times: list = {}):
    """
    「高斯消去法」的 LU 分解.

    本函数可以计算「列主元高斯消元法」、「顺序高斯消元法」的 LU 分解，
    通过参数 sequence 控制，默认 sequence=False 使用「列主元高斯消元法」。

    Args:
        a: np_array_like 方阵 (nxn)
        sequence: bool, True 则使用顺序高斯消去法，False 为列主元的高斯消去法
            default: sequence=False
        swap_times: 这是一个**输出**用的变量，只有传入 dict 变量时才有效。
            若使用「列主元高斯消元法」（sequence=False）
            则，置 swap_times['swap_times'] = 行交换次数。
            这个值正常的输出中不需要，但在一些问题，比如，
            利用 LU 分解求行列式时，得到 swap_times 会很有帮助。

    Returns:
        (l, u, p): result

        l: np.array, Lower triangle result (nxn)
        u: np.array, Upper triangle result (nxn)
        p: np.array, Permutation: 交换后的行顺序 (n)
            p = None if sequence=True

    Raises:
        Exception: 存在为零的主元素
    """
    a = np.array(a, dtype=np.float)  # copy

    assert a.shape[0] == a.shape[1]
    n = a.shape[0]

    if not sequence:
        # p 记录行交换的过程，使用「列主元高斯消元法」才使用，否则为 None
        p = np.array([k for k in range(n)])
        # swap_times:  行交换次数
        if isinstance(swap_times, dict):
            swap_times['swap_times'] = 0
    else:
        p = None

    for k in range(n-1):
        if not sequence:
            i_max = k + np.argmax(np.abs(a[k:n, k]))

            if i_max != k:
                a[[i_max, k]] = a[[k, i_max]]  # swap rows
                p[[i_max, k]] = p[[k, i_max]]  # record
                swap_times['swap_times'] += 1

        if a[k][k] == 0:
            raise Exception("存在为零的主元素")

        for i in range(k+1, n):
            a[i][k] /= a[k][k]  # L @ 严格下三角
            for j in range(k+1, n):
                a[i][j] -= a[i][k] * a[k][j]  # U @ 上三角

    # print(a, p)

    # Uncommit the following lines to get a Permutation Matrix
    # Only for sequence=False
    # pm = np.zeros_like(a)
    # for i, v in enumerate(p):
    #     pm[i, v] = 1
    #     print(pm)

    return np.tril(a, k=-1) + np.identity(a.shape[0]), np.triu(a), p


def solve_lu(b, l, u, p=None):
    """用 lu(a) 得到的 `pa=lu` 分解的结果求解原方程组 `ax=b` 的解 x。

    若 p 不为 None 则使用「列主元高斯消元」，p 为 None表示使用「顺序高斯消元」。

        # `@` means matrix multiplication, refer: https://docs.python.org/reference/expressions.html#binary-arithmetic-operations
        b = p @ b if p != None
        l @ y = b
        u @ x = y

    Args:
        b: np_array_like, 原方程组的右端常数（n）
        l: np_array_like, Lower triangle of lu_seq(a)
        u: np_array_like, Upper triangle of lu_seq(a)
        p: np_array_like, LU分解中交换后的行顺序
            default p=None: 未做行交换，即使用顺序高斯消去法

        使用列主元高斯消元法时，l, u, p 使用 lu(a) 得到的结果即可：
            solve_lu(b, *lu(a))
        或者使用顺序高斯消元：
            solve_lu(b, *lu(a, sequence=True))  # p=None

    Returns:
        x : np.array `ax=b` 的解（n）
    """
    assert np.shape(l) == np.shape(u)
    assert np.shape(l)[0] == np.shape(b)[0]

    n = np.shape(l)[0]

    # do swap
    if p is not None:
        b = [b[v] for v in p]

    # L * y = b
    y = np.zeros(n, dtype=np.float)
    y[0] = b[0]
    for i in range(1, n):
        bi = b[i]
        for j in range(0, i):
            bi -= y[j] * l[i][j]
        y[i] = bi / l[i][i]
    # print(y)

    # U * x = y
    x = np.zeros(n, dtype=np.float)
    x[n-1] = y[n-1] / u[n-1][n-1]
    for i in range(n-2, -1, -1):  # from n-2 (included) to 0 (included)
        yi = y[i]
        for j in range(i+1, n):
            yi -= x[j] * u[i][j]
        x[i] = yi / u[i][i]
    # print(x)

    return x


def det(a):
    """矩阵行列式

    利用 LU 分解（列主元高斯消元）求方阵 a 的行列式: d = det(a)

    Args:
        a: np_array_like, 要求行列式的矩阵

    Returns:
        d: float, a 的行列式值。

    Reference:
        https://blog.csdn.net/nstarLDS/article/details/106074256
    """
    swap_times = {}
    l, u, p = lu(a, sequence=False, swap_times=swap_times)
    sign = -1 if swap_times['swap_times'] % 2 == 1 else 1
    return np.prod(np.diag(u)) * sign


def inv(a):
    """矩阵的逆

    利用 LU 分解（列主元高斯消元）求方阵 a 的逆矩阵: x = inv(a)

    Args:
        a: np_array_like, 待求逆的矩阵

    Returns:
        x: float, a 的逆矩阵

    Reference:
        https://en.wikipedia.org/wiki/LU_decomposition#Inverting_a_matrix
    """
    l, u, p = lu(a)

    X = np.zeros_like(a, dtype=np.float)
    B = np.identity(np.shape(a)[0])

    for i, b in enumerate(B.T):  # iter on cols
        x = solve_lu(b, l, u, p)
        X[:, i] = x

    return X
