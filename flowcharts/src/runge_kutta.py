def runge_kutta(f, a, b, h, y0):
    
    BLOCK = 0
    x = a
    y = y0

    while x <= b or abs(b - x) < 1e-14:    # x <= b
        yield (x, y)

        BLOCK = 1
        k1 = f(x, y)
        k2 = f(x + h / 2, y + h * k1 / 2)
        k3 = f(x + h / 2, y + h * k2 / 2)
        k4 = f(x + h, y + h * k3)
        
        BLOCK = 2
        x = x + h
        y = y + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6