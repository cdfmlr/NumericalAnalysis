from sympy import *


# 差商缓存
__difference_quotient_cache = {}


def difference_quotient(f, xs: list, verbose=False):
    """求差商 $f[xs...]$

    Args:
        f: function, 函数
        xs: list, 要计算的差商的 $f[x0, x1, ...]$ 的参数值：[x0, x1, ...]
        verbose: bool, 打印出每一步计算差商的值, default False

    Returns:
        dq: sympy object, 差商值
    """

    # 尝试从缓存读取
    __key = str([(x, f(x)) for x in xs])
    if __key in __difference_quotient_cache:
        if verbose:
            print(f"cached: f{xs}: {__difference_quotient_cache[__key]}")
        return __difference_quotient_cache[__key]

    if len(xs) == 1:  # 0阶
        dq = sympify(f(xs[0]))
    else:  # n 阶
        dq_h = difference_quotient(f, xs[:-1], verbose)
        dq_l = difference_quotient(f, xs[1:], verbose)
        dq = (dq_l - dq_h) / (xs[-1] - xs[0])

    if verbose:
        print(f"f{xs}: {dq}")

    # 写入缓存
    __difference_quotient_cache[__key] = dq

    return dq
