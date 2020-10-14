from sympy import *
from difference_quotient import difference_quotient


def newton_interpolate(points: list, N_start=0, points_start=[], simplify_result=True, verbose=False):
    """牛顿插值

    Args:
        points: [(x1, y1), (x2, y2), ..., (xn, yn)]： 插值点

        N_start: a sympy object of Symbol('x'), 起始插值多项式。
        points_start: [(x1, y1), (x2, y2), ..., (xn, yn)]: 计算 N_start 用的插值点
                 该函数中做的插值会「承袭」这个用 points_start 计算的 N_start，在其基础上用新增插值点 points 去改进。
                 default 0 (从头开始构建).

        simplify_result: bool, 化简最终结果, default True
        verbose: 打印出每一步计算差商的值, default False

    Returns: 
        N: a sympy object of Symbol('x'), 插值多项式 $N(x)$
    """
    x = Symbol('x')

    # sympify points
    # for i in range(len(points)):
    #     points[i] = sympify(points[i][0]), sympify(points[i][1])

    def f(x): return dict(points + points_start)[x]

    xs = [p[0] for p in points_start]  # 承袭的插值点
    N = N_start   # 承袭的插值多项式
    for point in points:
        xs.append(point[0])
        N += difference_quotient(f, xs, verbose) * \
            prod([x - xi for xi in xs[:-1]])

    if simplify_result:
        N = simplify(N)
    return N


if __name__ == "__main__":
    points = [(11, 0.190809), (12, 0.207912), (13, 0.224951)]

    N = newton_interpolate(points)
    print('插值多项式:', N)
    print('Hypothesis:  ', N.subs(Symbol('x'), 11.5))
    print('Actual vaule:', sin(rad(11.5)).evalf())

    # 承袭之前的 N:
    print('承袭:')
    new_points = [(11.2, sin(rad(11.2)).evalf()),
                  (11.7, sin(rad(11.7)).evalf())]
    N1 = newton_interpolate(new_points, N_start=N,
                            points_start=points, verbose=True)
    print('插值多项式:', N1)
    print('Hypothesis:  ', N1.subs(Symbol('x'), 11.5).evalf())
    print('Actual vaule:', sin(rad(11.5)).evalf())
