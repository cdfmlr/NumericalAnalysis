# 该文件中实现了 Romberg 求积方法。
#
# - romberg_integral(f, a, b, epsilon, max_iter=10000): Romberg 法积分
# - romberg_integral_sw(f, a, b, epsilon, max_iter=10000): Romberg 法积分，滑动窗口版
#
# Copyright 2020 CDFMLR. All rights reserved.


def romberg_integral(f, a, b, epsilon, max_iter=10000):
    """Romberg 积分

    该函数保留完整的计算过程（输出T）。
    对于需要迭代计算到 m > 4 的问题，如果不需要这些过程量，使用 romberg_integral_sw 代替该函数可以有效节省内存。

    Args:
        f: 要求积的函数
        a, b: 求积区间
        epsilon: 目标精度，达到则停止，返回积分值
        max_iter: 最大迭代次数，超出这个次数迭代不到目标精度，则 raise 一个 RuntimeError

    Returns:
        result, T, iter

        result: 最终得到的积分值
        T: 计算过程表
        iter_times: 迭代次数

    Raises:
        RuntimeError: 无法在 max_iter 步内迭代到目标精度
    """
    m = 0

    T = [[None] * 4]
    T[0][0] = (b - a) * (f(a) + f(b)) / 2

    for m in range(1, int(max_iter)):
        T.append([None] * 4)

        h = (b - a) / (2 ** m)

        _s = sum((f(a + (2 * k - 1) * h) for k in range(1, 1 + 2**(m-1))))
        T[m][0] = T[m-1][0] / 2 + h * _s

        _t = 4      # 4 ** 1
        T[m-1][1] = (_t * T[m][0] - T[m-1][0]) / (_t - 1)

        if m > 1:
            _t *= 4  # 4 ** 2
            T[m-2][2] = (_t * T[m-1][1] - T[m-2][1]) / (_t - 1)
        if m > 2:
            _t *= 4  # 4 ** 3
            T[m-3][3] = (_t * T[m-2][2] - T[m-3][2]) / (_t - 1)

        if (m > 3) and (abs(T[m-3][3] - T[m-4][3]) < epsilon):
            break
        # End for
    else:
        raise RuntimeError('无法在 max_iter 步内迭代到目标精度')

    return T[m-3][3], T, m


def romberg_integral_sw(f, a, b, epsilon, max_iter=10000):
    """Romberg 积分

    用滑动窗口改写了 romberg_integral。
    在计算的过程中，不断删除不再需要的值，
    对于需要多次迭代的问题，可以有效节省内存。

    P.S. 这里说的「节省内存」只是理论上的。实际的测试中，我没有找到需要太多次迭代的求积函数来进行严格比较。

    Args:
        f: 要求积的函数
        a, b: 求积区间
        epsilon: 目标精度，达到则停止，返回积分值
        max_iter: 最大迭代次数，超出这个次数迭代不到目标精度，则 raise 一个 RuntimeError

    Returns:
        result, T, iter

        result: 最终得到的积分值
        T: 计算过程表（只有最后的 m-4 到 m 步）
        iter_times: 迭代次数

    Raises:
        RuntimeError: 无法在 max_iter 步内迭代到目标精度
    """
    m = 0

    T = [[None] * 4]
    T[0][0] = (b - a) * (f(a) + f(b)) / 2

    for m in range(1, int(max_iter)):
        T.append([None] * 4)
        # 下面的索引 T[-1] 即 T_m, T[-2] 即 T_{m-1}, ...

        h = (b - a) / (2 ** m)

        _s = sum((f(a + (2 * k - 1) * h) for k in range(1, 1 + 2**(m-1))))
        T[-1][0] = T[-2][0] / 2 + h * _s

        _t = 4      # 4 ** 1
        T[-2][1] = (_t * T[-1][0] - T[-2][0]) / (_t - 1)

        if m > 1:
            _t *= 4  # 4 ** 2
            T[-3][2] = (_t * T[-2][1] - T[-3][1]) / (_t - 1)
        if m > 2:
            _t *= 4  # 4 ** 3
            T[-4][3] = (_t * T[-3][2] - T[-4][2]) / (_t - 1)

        if (m > 3) and (abs(T[-4][3] - T[-5][3]) < epsilon):
            break

        if (m > 4):
            T = T[1:]  # 清除不需要的
        # End for
    else:
        raise RuntimeError('无法在 max_iter 步内迭代到目标精度')

    return T[-4][3], T, m
