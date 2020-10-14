from sympy import *
import math


def bisection(f, a, b, eps, eta=1e-16, verbose=False):
    """二分法求根

    对方程 f(x) = 0 在区间 [a, b]，使用二分法求根。
    做 ceil((log(((b - a) / eps), 2) - 1) 次迭代，使结果满足精度 eps。

    实现参考: 数值分析[谷根代，杨晓忠 等著]2011年版.P18.算法1

    Args:
        f: function, 一元函数，表示要求根的方程: f(x) = 0.
        a, b: float, 有根区间 [a, b] 的端点.
        eps: float, 给定精度.

        eta: float, 当 abs(f(x)) <= eta 时停止计算, default 1e-16.
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

    N = math.ceil((log(((b - a) / eps), 2) - 1).evalf(5))

    if verbose:
        print(f'N = {N}\n')

    x = (a + b) / 2

    if verbose:
        print(f'n \t (a, b) \t f(x_n)')
        print('-'*35)

    for n in range(N+1):
        if abs(f(x)) <= eta:
            break

        if verbose:
            print(f'{n} \t ({a}, {b}) \t f({x})={f(x)}')

        if f(x) * f(a) < 0:
            b = x
        else:
            a = x
        x = (a + b) / 2
        n += 1

    if verbose:
        print(f'{n} \t ({a}, {b}) \t -')

    x_final = (a + b) / 2
    if verbose:
        print(f'\nresult: x = ({a}+{b})/2 = {x_final}')

    return x_final, N+1
