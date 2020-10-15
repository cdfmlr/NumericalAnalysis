# 该文件中实现了复化梯形、复化 Simpson 求积方法。
#
# - composite_trapezium_integral(f, a, b, epsilon, max_iter=10000): 复化梯形
# - composite_simpson_integral(f, a, b, epsilon, max_iter=10000): 复化 Simpson
#
# Copyright 2020 CDFMLR. All rights reserved.


def composite_trapezium_integral(f, a, b, epsilon, max_iter=10000):
    """复化梯形公式

    Args:
        f: 要求积的函数
        a, b: 求积区间
        epsilon: 目标精度，达到则停止，返回积分值
        max_iter: 最大迭代次数，超出这个次数迭代不到目标精度，则 raise 一个 RuntimeError

    Returns:
        i, iter
        i: 最终得到的积分值
        iter_times: 迭代次数

    Raises:
        RuntimeError: 无法在 max_iter 步内迭代到目标精度
    """
    m = 1
    h = b - a
    t = h * (f(a) + f(b)) / 2

    _iter_times = 0

    t_next = 0
    for _iter_times in range(int(max_iter)):
        h /= 2
        s = sum([f(a + (2 * k - 1) * h) for k in range(1, m+1)])
        t_next = t / 2 + h * s
        m <<= 1
        if abs(t_next - t) <= epsilon:
            break
        t = t_next
    else:
        raise RuntimeError('无法在 max_iter 步内迭代到目标精度')

    return t_next, _iter_times+1


def composite_simpson_integral(f, a, b, epsilon, max_iter=10000):
    """复化 Simpson 公式

    Args:
        f: 要求积的函数
        a, b: 求积区间
        epsilon: 目标精度，达到则停止，返回积分值
        max_iter: 最大迭代次数，超出这个次数迭代不到目标精度，则 raise 一个 RuntimeError

    Returns:
        i, iter
        i: 最终得到的积分值
        iter_times: 迭代次数

    Raises:
        RuntimeError: 无法在 max_iter 步内迭代到目标精度
    """
    m = 1
    h = (b - a) / 2
    i = h * (f(a) + 4 * f((a+b) / 2) + f(b)) / 3

    _iter_times = 0

    i_next = 0
    for _iter_times in range(int(max_iter)):
        h /= 2

        s0 = sum([f(a + (2 * k - 1) * h) for k in range(1, 2 * m + 1)])
        s1 = sum([f(a + (4 * k - 2) * h) for k in range(1, m + 1)])
        i_next = i / 2 + h * (4 * s0 - 2 * s1) / 3

        m <<= 1
        if abs(i_next - i) <= epsilon:
            break
        i = i_next
    else:
        raise RuntimeError('无法在 max_iter 步内迭代到目标精度')

    return i_next, _iter_times+1
