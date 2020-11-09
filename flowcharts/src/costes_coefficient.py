def costes_coefficient(n, k):

    ckn = ((-1) ** (n - k)) / n * factorial(k) * factorial(n - k)

    h = 1
    t = Symbol('t')
    for j in range(n+1):
        if j != k:
            h *= (t - j)

    ckn *= integrate(h, (t, 0, n))

    return ckn