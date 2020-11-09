def composite_trapezium_integral(f, a, b, epsilon, max_iter=10000):
    # m = 1
    # h = b - a
    # t = h * (f(a) + f(b)) / 2
    mht()

    # _iter_times = 0
    
    t_next = 0
    for _iter_times in range(int(max_iter)):
        h /= 2
        s = sum([f(a + (2 * k - 1) * h) for k in range(1, m+1)])
        t_next = t / 2 + h * s
        m <<= 1
        if abs(t_next - t) <= epsilon:
            break
        t = t_next
    else:
        raise RuntimeError('无法在 max_iter 步内迭代到目标精度')

    return t_next, _iter_times+1