from sympy import *
import math


def dichotomy(f, a, b, eps, eta=1e-16, verbose=False):
    """二分法求根

    对方程 f(x) = 0 在区间 [a, b]，使用二分法求根。
    一直迭代到 abs(b - a) <= eps 为止。

    实现参考：《实验二  非线性方程求根》

    Args:
        f: function, 一元函数，表示要求根的方程: f(x) = 0.
        a, b: float, 有根区间 [a, b] 的端点.
        eps: float, 根的容许误差.

        eta: float, abs(f(x)) 的容许误差, default 1e-16.
        verbose: bool, 打印出二分法计算的表格, default False.

    Returns:
        (x_final, N)

        x_final: float, 二分法求得的近似根
        N: int, 迭代次数

    Raises:
        ValueError: 给定的 f(a) * f(b) < 0 时无法求解，抛出异常
    """
    if f(a) * f(b) > 0:
        raise ValueError("rootless interval: f(a) * f(b) < 0")

    if verbose:
        print(f'n \t (a, b) \t f(x_n)')
        print('-'*35)

    n = 0
    while abs(b - a) > eps:
        x = (a + b) / 2
        fx = f(x)
        if verbose:
            print(f"{n}\t {a, b}\t f({x})={fx}")

        if abs(fx) <= eta:
            break

        if f(a) * fx < 0:
            b = x
        else:
            a = x

        n += 1

    x_final = (a + b) / 2
    if verbose:
        print(f"{n}\t {a, b}\t -")
        print(f'\nresult: x = ({a}+{b})/2 = {x_final}')

    return x_final, n
