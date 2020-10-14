from sympy import *


def lagrange_interpolate(points: list, simplify_result=True, verbose=False):
    """拉格朗日插值

    Args:
        points: list, [(x1, y1), (x2, y2), ..., (xn, yn)]
        simplify_result: bool, 化简最终结果, default True
        verbose: bool, 输出每一步的结果, default False

    Returns: 
        L: sympy object of Symbol('x'), 插值多项式 $L(x)$
    """
    x = Symbol('x')
    L = 0  # 插值多项式
    for i, point in enumerate(points):
        xi, yi = point
        li = 1
        for j in range(len(points)):
            if j == i:
                continue
            xj, yj = points[j]
            li *= (x - xj) / (xi - xj)
        L += yi * li
        if verbose:
            print(f"l_{i}(x) = ", simplify(yi * li))

    if simplify_result:
        L = simplify(L)
    return L
