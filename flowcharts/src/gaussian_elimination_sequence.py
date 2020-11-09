def gaussian_elimination_sequence(a, b):
    BLOCK = 0
    A = np.c_[a, b]  # 增广矩阵
    n = A.shape[0]
    x = np.zeros(n)

    # 消元
    for k in range(n-1):
        if A[k][k] == 0:
            raise Exception("求解失败")

        for i in range(k+1, n):
            m = A[i][k] / A[k][k];
            A[i][k] = 0;
            for j in range(k+1, n+1):
                A[i][j] -= A[k][j] * m

    # 回代
    x[n-1] = A[n-1][n] / A[n-1][n-1]
    for k in range(n-2, -1, -1): # from n-2 (included) to 0 (included)
        for j in range(k+1, n):
            A[k][n] -= A[k][j] * x[j]
        x[k] = A[k][n] / A[k][k]
        
    return x