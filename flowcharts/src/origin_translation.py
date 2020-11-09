def origin_translation(A, p, x0=None, eps=1e-8, max_steps=1000, verbose=False):        
        
    _I = identity(A.shape[0])
    
    BLOCK = 0
    eig = p
    x = x0
    
    for k in range(int(max_steps)):
        eig_prev = eig
        
        BLOCK = 1
        x = linalg.solve(A - eig * _I, x)
        q = argmax(abs(x))
        xq = x[q]
        
        BLOCK = 2
        eig = eig + 1 / xq
        x = x / xq
        
        if all(abs(eig - eig_prev) <= eps):
            break
    else:
        raise Exception(f"cannot reach eps ({eps}) after max_steps ({max_steps}). "
                                f"The last result: eig = {eig}, x={x}")
        
    return eig, x, k+1