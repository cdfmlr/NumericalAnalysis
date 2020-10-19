def runge_kutta_fehlberg(f, a, b, h_min, h_max, y0, eps):
    """Runge-Kutta-Fehlberg 方法（RKF）

    用 **Runge-Kutta-Fehlberg 方法**求如下常微分方程初值问题的数值解:

        y'(x) = f(x, y)  (for a <= x <= b)
        y(a) = y_0

    This function returns a generator that does lazy calculations，
    which generates solutions (x, y) of the equation for x from a to b by step h.

    Args:

        f: 二元函数，y'(x) = f(x, y)
        a, b: float, x 的区间端点
        h_min: float, 最小步长
        h_max: float, 最大步长
        y0: float, 初值 y(a)
        eps: float >= 0，容许误差

    Yields:

        (x, y)：方程的解 for x from a to b, step h.

    Raises:

        ValueError: (b > a) or (h_max < h_min) or (eps < 0)
        GeneratorExit: h_min too small. Failed to continue.

    """
    if b < a:
        raise ValueError("unexpected range [a, b] where b < a")
    if h_max < h_min:
        raise ValueError("unexpected step h_max < h_min ")
    if eps < 0:
        raise ValueError("unexpected eps < 0")

    h = h_max

    x = a
    y = y0

    yield (x, y)

    while x <= b:
        k1 = h * f(x, y)
        k2 = h * f(x + h / 4, y + k1 / 4)
        k3 = h * f(x + 3 * h / 8, y + 3 * k1 / 32 + 9 * k2 / 32)
        k4 = h * f(x + 12 * h / 13, y + 1932 / 2197 *
                   k1 - 7200 / 2197 * k2 + 7296 / 2197 * k3)
        k5 = h * f(x + h, y + 439 / 216 * k1 - 8 * k2 +
                   3680 / 513 * k3 - 845 / 4104 * k4)
        k6 = h * f(x + h / 2, y - 8 / 27 * k1 + 2 * k2 - 3544 /
                   2565 * k3 + 1859 / 4104 * k4 - 11 / 40 * k5)

        R = abs(k1 / 360 - 128 / 4275 * k3 - 2197 /
                75240 * k4 + k5 / 50 + 2 / 55 * k6)

        if R <= h * eps:
            x = x + h
            y = y + k1 * 25 / 216 + 1408 / 2565 * k3 + 2197 / 4104 * k4 - k5 / 5
            yield (x, y)

        delta = 0.84 * (eps * h / R) ** (1/4)

        if delta <= 0.1:
            h = 0.1 * h
        elif delta >= 4:
            h = 4 * h
        else:
            h = delta * h

        if h > h_max:
            h = h_max

        if abs(x - b) < eps:
            break

        if x + h > b:
            h = b - x

        if h < h_min:
            raise GeneratorExit("h_min too small. Failed to continue.")
