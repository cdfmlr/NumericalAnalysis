from sympy import *
import math


def single_point_truncation(f, x_0, x_1, eps=0, eta=0, max_steps=20, verbose=False):
    """单点弦截法

    Args: 
        f: function, 迭代函数
        x_0, x_1: float, 初值
        eps: float, 根的容许误差, default 0.
        eta: float, abs(f(x)) 的容许误差, default 0.

        max_steps: int, 最大迭代次数, default 20.
        verbose: bool, 打印出每一步的值, default False.

    Returns: 
        x_final: float, 最终的近似根 x
    """

    f_x0 = f(x_0)

    x = x_1
    for i in range(max_steps):
        if verbose:
            print(i, x)

        x_next = x - f(x) / (f(x) - f_x0) * (x - x_0)

        if abs(x_next - x) <= eps or abs(f(x)) <= eta:
            break

        x = x_next

    return x
