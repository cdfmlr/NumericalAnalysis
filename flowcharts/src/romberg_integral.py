def romberg_integral(f, a, b, epsilon, max_iter=1e6):
    m = 0


    # T = [[None] * 4]
    # T[0][0] = (b - a) * (f(a) + f(b)) / 2
    BLOCK = 0

    for m in range(1, int(max_iter)):
        T.append([None] * 4)
        
        h = (b - a) / (2 ** m)
        
        # _s = sum((f(a + (2 * k - 1) * h) for k in range(1, 1 + 2**(m-1))))
        # T[m][0] = T[m-1][0] / 2 + h * _s
        BLOCK = 1
        
        # _t = 4      # 4 ** 1
        # T[m-1][1] = (_t * T[m][0] - T[m-1][0]) / (_t - 1)
        BLOCK = 2

        if m > 1:
            BLOCK = 3
            return 
            # _t *= 4  # 4 ** 2
            # T[m-2][2] = (_t * T[m-1][1] - T[m-2][1]) / (_t - 1)
        if m > 2:
            BLOCK = 4
            return
            # _t *= 4  # 4 ** 3
            # T[m-3][3] = (_t * T[m-2][2] - T[m-3][2]) / (_t - 1)
        
        if (m > 3) and (abs(T[m-3][3] - T[m-4][3]) < epsilon):
            break
        # End for
    else:
        raise RuntimeError('无法在 max_iter 步内迭代到目标精度')

    return T[m-3][3], T, m