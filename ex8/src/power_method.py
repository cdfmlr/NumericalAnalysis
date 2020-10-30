import numpy as np


def power_iteration(A, m0=1, u0=None, eps=1e-8, max_steps=500, verbose=False):
    """正幂法（power iteration a.k.a. the power method）计算矩阵 A 的按模最大特征值、特征向量

    Args:
        A:   np_array_like 待求特征值的矩阵 (nxn)
        m0:  float 初始特征值
                default m0=1
        u0: np_array_like 初始特征向量（n）
                default u0=None: 取 u0 = (1, 1, ..., 1)
        eps: float 精度要求
                default eps=1e-8
        max_steps: int 最大迭代次数
                default max_steps=1000
        verbose: bool, 若为 True 则打印出每一步的结果
                default verbose=False

    Returns:
        (m, u, k): 在 max_steps 次迭代以内得到第一组的满足 eps 的结果
            m: float 所求主特征值
            u: np.array 相应的特征向量
            k: int 迭代次数

    Raises:
        ValueError: 参数 A 不是方阵，
                    或 A 和给定 u0 尺寸不匹配
        Exception:  无法在max_steps 次迭代以内得到满足精度 eps 的结果
    """

    _shape = np.shape(A)
    if len(_shape) < 2 or _shape[0] != _shape[1]:
        raise ValueError(f"unexpected A, shape: {_shape}")

    if u0 is not None:
        if len(u0) != _shape[0]:
            raise ValueError(
                f"A (shape={_shape}) and u0 (len={len(u0)}) not match")
    else:  # not u0
        u0 = np.ones(_shape[0])

    m = m0
    u = u0

    for k in range(int(max_steps)):
        if verbose:
            print(k, m, u)

        m_prev = m

        v = np.dot(A, u)
        mi = np.argmax(np.abs(v))
        m = v[mi]
        u = v / m

        if abs(m - m_prev) <= eps:
            break

    else:
        raise Exception(f"cannot reach eps ({eps}) after max_steps ({max_steps}). "
                        f"The last result: m = {m}, u={u}")

    if verbose:
        print('result of power_iteration:', m, u, k+1)

    return m, u, k+1
