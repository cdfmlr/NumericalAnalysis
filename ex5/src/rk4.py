def runge_kutta(f, a, b, h, y0):
    """四阶龙格-库塔法的算法: (generally referred to as RK4)

    用经典**四阶龙格-库塔算法**求如下常微分方程初值问题的数值解:

        y'(x) = f(x, y)  (for a <= x <= b)
        y(a) = y_0

    This function returns a generator that does lazy calculations，
    which generates solutions (x, y) of the equation for x from a to b by step h.

    Args:

        f: 二元函数，y'(x) = f(x, y)
        a, b: float, x 的区间
        h: float , x 迭代步：x_0 = a，x_1 = x_0 + h, x_2 = x_1 + h, ..., x_n = x_{n-1} + h = b
        y0: float, 初值 y(a)

    Yields:

        (x, y)：方程的解 for x from a to b, step h.

    Raises:

        ValueError: (b < a) or (h <= 0)
    """
    if b < a:
        raise ValueError("unexpected range [a, b] where b < a")
    if h <= 0:
        raise ValueError("unexpected step h <= 0")

    x = a
    y = y0

    while x <= b or abs(b - x) < 1e-14:    # x <= b
        yield (x, y)

        k1 = f(x, y)
        k2 = f(x + h / 2, y + h * k1 / 2)
        k3 = f(x + h / 2, y + h * k2 / 2)
        k4 = f(x + h, y + h * k3)

        x = x + h
        y = y + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
