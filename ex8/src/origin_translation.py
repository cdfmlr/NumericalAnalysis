import numpy as np


def origin_translation(A, p, x0=None, eps=1e-8, max_steps=1000, verbose=False):
    """原点位移算法
    (搜不到这个方法英文是什么)

    Args:
        A:  np_array_like, 待求特征值的矩阵 (nxn)
        p:  float 位移因子
        x0: np_array_like, 初始向量（n）, 要求 max(abs(x0)) == 1
                default x0=None: 取 x0 = (1, 1, ..., 1)
        eps: float, 控制精度
                default eps=1e-8
        max_steps: 最大迭代次数
                default max_steps=1000
        verbose: 打印出每步的结果，default verbose=False

    Returns:
        (eig, x, k)
            eig: float, A 的靠近 p 的特征值
            x: np.array, 单位化的特征向量
            k: int, 迭代次数

    Raises:
        ValueError: 参数 A 不是方阵，
                    或 A 和给定 x0 尺寸不匹配
                    或 x0 = 0
                    或 max(u0) != 1
        Exception:  无法在max_steps 次迭代以内得到满足精度 eps 的结果
    """

    _shape = np.shape(A)
    if len(_shape) < 2 or _shape[0] != _shape[1]:
        raise ValueError(f"unexpected A, shape: {_shape}")

    if x0 is not None:
        if len(x0) != _shape[0]:
            raise ValueError(
                f"A (shape={_shape}) and x0 (len={len(x0)}) not match")
        if np.all(x0 == 0):
            raise ValueError(f'bad x0: x0 == 0')
    else:  # not u0
        x0 = np.ones(_shape[0])

    _I = np.identity(_shape[0])

    eig = p
    x = x0

    for k in range(int(max_steps)):
        if verbose:
            print(k, eig, x)

        eig_prev = eig

        try:
            x = np.linalg.solve(A - eig * _I, x)
        except np.linalg.LinAlgError as e:
            # traceback.print_exc()
            x = np.linalg.solve(A - eig * _I + eps, x)

        q = np.argmax(np.abs(x))
        xq = x[q]

        eig = eig + 1 / xq

        x = x / xq

        if np.all(np.abs(eig - eig_prev) <= eps):
            break
    else:
        raise Exception(f"cannot reach eps ({eps}) after max_steps ({max_steps}). "
                        f"The last result: eig = {eig}, x={x}")

    if verbose:
        print('result of origin_translation:', eig, x, k+1)

    return eig, x, k+1
