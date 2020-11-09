def adaptsim(f, a, b, eps=1e-8, max_iter=10000):

    BLOCK = 0
    p = [a, b]  # 分点
    p0 = p
    ep = [eps]
    m = 0
    q = 0
    I = 0
    
    for _iter_times in range(int(max_iter)):
        BLOCK = 2
        n1 = len(ep)
        n = len(p0)
        
        if n <= 1:
            break
        
        h = p0[1] - p0[0]

        BLOCK = 3
        s0 = h /  6 * ( f(p0[0]) + 4 * f(p0[0] + h/2) + f(p0[0] + h  ) )
        s1 = h / 12 * ( f(p0[0]) + 4 * f(p0[0] + h/4) + f(p0[0] + h/2) )
        s2 = h / 12 * ( f(p0[0] + h/2) + 4 * f(p0[0] + 3*h/4) + f(p0[0] + h) )
        
        if abs(s0 - s1 - s2) <= 15 * ep[0]:
            I += s1 + s2
            p0 = p0[1:]
            
            if n1 >= 2:
                ep = ep[1:]
            
            q += 1
        else:
            m += 1

            p0 = [p0[0], p0[0] + h/2] + p0[1:]
            
            ep = [ep[0]/2, ep[0]/2] if n1 == 1 else [ep[0]/2, ep[1]/2] + ep[1:]

            p = p0 if q == 0 else p[:q] + p0
            
    else:
        raise Exception('无法在 max_iter 步内迭代到目标精度')

    return I, m, p