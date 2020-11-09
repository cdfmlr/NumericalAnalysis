def spline3_interpolate(points: list, simplify_result=True):
    # 排序给定的点
    ps = sorted(points, key=lambda p: p[0])
    
    n = len(points)

    # points to a function
    _f_dict = dict(ps)
    f = lambda x:  _f_dict[x]

    # $h_k = x_{k+1} - x_k$
    h = lambda k: ps[k+1][0] - ps[k][0]

    hks = [h(0)]

    # 用方程 D * M = d 解出 M

    D = np.zeros((n, n))
    d = np.zeros(n)

    for k in range(1, n-1):
        # $h_k$, $h_{k-1}$
        hks.append(h(k))
        hk, hks1 = hks[k], hks[k-1]

        # $\mu_k$ -> mu, $\lambda_k$ -> ld
        _fra = hks1 + hk
        mu = hks1 / _fra
        ld = hk / _fra

        # $\mu_kM_{k-1}+2M_k+\lambda_kM_{k+1} = d_k$
        D[k, k-1] = mu
        D[k, k]   = 2
        D[k, k+1] = ld
        d[k] = 6 * difference_quotient(f, [ps[k-1][0], ps[k][0], ps[k+1][0]])

    # 边界条件
    # Natural Boundary
    D[0, 0] = 1
    D[n-1, n-1] = 1

    d[0] = 0
    d[n-1] = 0

    # 解出 M
    M = np.linalg.solve(D, d)

    # 插值函数
    piecewises = []
    for k in range(n-1):
        s  = M[k] * (ps[k+1][0] - _x) ** 3 / (6 * hks[k])
        s += M[k+1] * (_x - ps[k][0]) ** 3 / (6 * hks[k])
        s += (ps[k][1] - M[k] * hks[k]**2 / 6) * (ps[k+1][0] - _x) / hks[k]
        s += (ps[k+1][1] - M[k+1] * hks[k]**2 / 6) * (_x - ps[k][0]) / hks[k]
        if simplify_result:
            s = simplify(s)
        piecewises.append((s, And(_x >= ps[k][0], _x <= ps[k+1][0])))

    return Piecewise(*piecewises)