def adaptsim(f, a, b, eps=1e-8, max_iter=10000):
    """自适应 Simpson 求积
    
    P.S. 这个函数名来自 Gander, W. and W. Gautschi, “Adaptive
         Quadrature – Revisited,” BIT, Vol. 40, 2000, pp. 84-101.
         该文档可以在 https://people.inf.ethz.ch/gander/ 找到。
         但该函数的实现并没有使用此文中的递归方法。

    Args:
        f: 要求积的函数
        a, b: 求积区间
        eps: 目标精度，达到则停止，返回积分值
        max_iter: 最大迭代次数，超出这个次数迭代不到目标精度，则 raise 一个 Exception

    Returns: (I, m, p)
        I: 积分的近似值
        m: 分层数
        p: 分点

    Raises:
        Exception: 无法在 max_iter 步内迭代到目标精度
    """
    p = [a, b]  # 分点
    p0 = p
    ep = [eps]
    m = 0
    q = 0
    I = 0
    
    for _iter_times in range(int(max_iter)):
        n1 = len(ep)
        n = len(p0)
        
        if n <= 1:
            break
        
        h = p0[1] - p0[0]
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
            
            if n1 == 1:
                ep = [ep[0]/2, ep[0]/2]
            else:
                ep = [ep[0]/2, ep[1]/2] + ep[1:]
            
            if q == 0:
                p = p0
            else:
                p = p[:q] + p0
        
    else:
        raise Exception('无法在 max_iter 步内迭代到目标精度')

    return I, m, p


def asr(f, a, b, eps=1e-8):
    """自适应 Simpson 求积的递归实现
    
    Args:
        f: 要求积的函数
        a, b: 求积区间
        eps: 目标精度，达到则停止，返回积分值

    Returns: 
        I: 计算结果：积分的近似值
    """
    def simpson(f, a, b):
        return (b - a) * (f(a) + 4 * f((a + b) / 2) + f(b)) / 6
    
    def asrp(f, a, b, eps, sim):
        mid = (a + b) / 2
        L = simpson(f, a, mid)
        R = simpson(f, mid, b)

        if (abs(L + R - sim) <= eps):
            return L + R + (L + R - sim) / 15
        
        return asrp(f, a, mid, eps/2, L) + asrp(f, mid, b, eps/2, R)
    
    return asrp(f, a, b, eps, simpson(f, a, b))