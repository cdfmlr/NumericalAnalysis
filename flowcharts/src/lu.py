def lu(a, sequence=False, swap_times: list = {}):

    n = a.shape[0]
    
    p =  np.array([k for k in range(n)])# p 记录行交换的过程，使用「列主元高斯消元法」才使用，否则为 None
    swap_times = 0# swap_times:  行交换次数
    
    for k in range(n-1):
        if not sequence:
            i_max = k + np.argmax(np.abs(a[k:n, k]))

            if i_max != k:
                swap_rows(a, i_max, k)
                swap_item(p, i_max, k)  # record swap in p
                swap_times += 1  # swap_times += 1
        
        if a[k][k] == 0:
            raise Exception("存在为零的主元素")
            
        for i in range(k+1, n):
            a[i][k] /= a[k][k]  # L @ 严格下三角
            for j in range(k+1, n):
                a[i][j] -= a[i][k] * a[k][j]  # U @ 上三角
    
    return np.tril(a, k=-1) + np.identity(a.shape[0]), np.triu(a), p