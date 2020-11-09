def dichotomy(f, a, b, eps, eta=1e-16, verbose=False):
    if f(a) * f(b) > 0:
        raise ValueError("rootless interval: f(a) * f(b) < 0")
    
    if verbose:
        print(f'n \t (a, b) \t f(x_n)')
    
    n = 0
    while abs(b - a) > eps:
        x = (a + b) / 2
        fx = f(x)

        if abs(fx) <= eta:
            break
        
        if f(a) * fx < 0:
            b = x
        else:
            a = x
        
        n += 1

    x_final = (a + b) / 2
    if verbose:
        print(f'\nresult: x = ({a}+{b})/2 = {x_final}')
    
    return x_final, n
