def lagrange_interpolate(points: list, simplify_result=True, verbose=False):
    x = Symbol('x')
    L = 0  # 插值多项式
    for i, (xi, yi) in enumerate(points):
        li = 1
        for j in range(len(points)):
            if j == i:
                continue
            xj, yj = points[j]
            li *= (x - xj) / (xi - xj)
        L += yi * li

    return L