def power_iteration(A, m0=1, u0=None, eps=1e-8, max_steps=500, verbose=False):
    m = m0
    u = u0

    for k in range(int(max_steps)):
        if verbose:
            print(k, m, u)
        
        m_prev = m
        
        v = dot(A, u)
        mi = argmax(abs(v))
        m = v[mi]
        u = v / m
        
        if abs(m - m_prev) <= eps:
            break
            
    else:
        raise Exception(f"cannot reach eps after max_steps."
                        f"The last result: m = {m}, u={u}")

    return m, u, k+1