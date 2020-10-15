# 该文件中实现了各种 Newton-Cotes 求积方法，包括：
#
# - trapezium_integral(f, a, b): 梯形求积公式
# - simpson_integral(f, a, b): 辛普森求积公式
# - costes_coefficient(n, k): 求柯特斯系数
# - newton_cotes_integral(f, a, b, n): 牛顿-科特斯求积公式
#
# Copyright 2020 CDFMLR. All rights reserved.


from sympy import *


def trapezium_integral(f, a, b):
    """梯形求积公式
    """
    return (b - a) * (f(a) + f(b)) / 2


def simpson_integral(f, a, b):
    """辛普森求积公式
    """
    return (b - a) * (f(a) + 4 * f((a + b) / 2) + f(b)) / 6


def costes_coefficient(n, k):
    """求柯特斯系数
    """
    ckn = ((-1) ** (n - k))
    ckn /= n * factorial(k) * factorial(n - k)

    h = 1
    t = Symbol('t')
    for j in range(n+1):
        if j != k:
            h *= (t - j)

    ckn *= integrate(h, (t, 0, n))

    return ckn


def newton_cotes_integral(f, a, b, n):
    """牛顿-科特斯求积公式
    """
    step = (b - a) / n
    xs = [a + i * step for i in range(n+1)]
    return (b - a) * sum([costes_coefficient(n, k) * f(xs[k]) for k in range(0, n+1)])
