def improved_euler(f, a, b, h, y0):    
    x = a
    y = y0

    while x <= b or abs(b - x) < 1e-14:    # x <= b
        yield (x, y)

        y_next_g = y + h * f(x, y)
        y_next = y + h * ( f(x, y) + f(x+h, y_next_g) ) / 2
        
        x = x + h
        y = y_next