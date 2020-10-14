from sympy import *
import math


def fixed_point_iter(phi, x_0, max_steps=25, verbose=False):
    """不动点迭代

    Args: 
        phi: function, 迭代函数
        x_0: float, 初值

        max_steps: int, 最大迭代次数
        verbose: bool, 打印出每一步的值，default False.

    Returns: 
        x_final: float, 最终的近似根 x 
    """
    x = x_0
    for i in range(max_steps):
        if verbose:
            print(f'x_{i} \t {x}')
        x = phi(x)
    return x
