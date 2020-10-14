from sympy import *
import math


def newton_iter(f, x_0, eps=0, eta=0, df=None, max_steps=20, frac=False, verbose=False):
    """牛顿迭代法

    Args: 
        f: function, 迭代函数
        x_0: float, 初值
        eps: float, 根的容许误差, default 0.
        eta: float, abs(f(x)) 的容许误差, default 0.

        df: function, f 的导函数, 默认 None 表示自动调用 sympy.diff 求导(会导致后续迭代中使用分数运算)。
        max_steps: int, 最大迭代次数, default 20.
        frac: bool, True 则输出分数(仅对 df=None 时生效)，否则使用 float, default False.
        verbose: bool, 打印出每一步的值, default False.

    Returns: 
        x_final: float, 最终的近似根 x
    """

    if df == None:
        __x = Symbol('x')
        __df = diff(f(__x), __x)

        df = lambda x: __df.subs(__x, x)

    x = x_0
    for i in range(max_steps):
        if verbose:
            print(i, x)

        x_next = x - f(x) / df(x)

        if abs(x_next - x) <= eps or abs(f(x)) <= eta:
            break

        x = x_next

    if not frac:
        x = float(x)
    return x
