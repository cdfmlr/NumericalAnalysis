def jacobi_iter(A, b, x0=None, eps=1e-5, max_steps=5000, verbose=False):

        
    # A =  D - L - U
    
    BLOCK = 0
    D = diag(diag(A))
    L = - tril(A, -1)
    U = - triu(A, 1)
    
    BLOCK = 1
    B = inv(D) @ (L + U)
    f = inv(D) @ b
    
    BLOCK = 3
    # x = x0
    # i = 0
    for i in range(int(max_steps)):
        x_prev = x
        
        x = B @ x + f
        
        if all(abs(x - x_prev) <= eps):  # 达到精度要求
            break
    else:
        raise Exception(f"cannot reach eps ({eps}) after max_steps ({max_steps}). The last result: x = {x}")

    return x