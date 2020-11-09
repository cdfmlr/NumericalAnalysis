def runge_kutta_fehlberg(f, a, b, h_min, h_max, y0, eps):

    BLOCK = 0
    h = h_max
    x = a
    y = y0

    yield (x, y)

    while x <= b:
        BLOCK = 1
        k1 = h * f(x, y)
        k2 = h * f(x + h / 4, y + k1 / 4)
        k3 = h * f(x + 3 * h / 8, y + 3 * k1 / 32 + 9 * k2/ 32)
        k4 = h * f(x + 12 * h / 13, y + 1932 / 2197 * k1 - 7200 / 2197 * k2  + 7296 / 2197 * k3 )
        k5 = h * f(x + h, y + 439 / 216 * k1 - 8 * k2 + 3680 / 513 * k3 - 845 / 4104 * k4)
        k6 = h * f(x + h / 2, y - 8 / 27 * k1 + 2 * k2 - 3544 / 2565 * k3 + 1859 / 4104 * k4 - 11 / 40 * k5)

        R = abs(k1 / 360 - 128 / 4275 * k3 - 2197 / 75240 * k4 + k5 / 50 + 2 / 55 * k6)

        if R <= h * eps:
            BLOCK = 2
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