from sympy import *
import math


def secant_method(f, x0, x1, eps=0, eta=0, max_steps=20, verbose=False):
    """两点弦截法（割线法）

    Args: 
        f: function, 迭代函数
        x0, x1: float, 初值
        eps: float, 根的容许误差, default 0.
        eta: float, abs(f(x)) 的容许误差, default 0.

        max_steps: int, 最大迭代次数, default 20.
        verbose: bool, 打印出每一步的值, default False.

    Returns: 
        x_final: float, 最终的近似根 x
    """
    for i in range(max_steps):
        if verbose:
            print(i, x1)

        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0, x1 = x1, x2

        if abs(x1 - x0) <= eps or abs(f(x1)) <= eta:
            break

    return x1
