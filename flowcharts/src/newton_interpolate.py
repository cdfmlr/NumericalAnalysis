def newton_interpolate(points: list, N_start=0, points_start=[], simplify_result=True, verbose=False):
    x = Symbol('x')
    

    f = lambda x: dict(points + points_start)[x]
    
    xs = [p[0] for p in points_start] # 承袭的插值点
    N = N_start   # 承袭的插值多项式
    for point in points:
        xs.append(point[0])
        N += difference_quotient(f, xs, verbose) * prod([x - xi for xi in xs[:-1]])
    
    if simplify_result:
        N = simplify(N)
    return N