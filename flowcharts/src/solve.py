def solve():
    x = np.zeros(n, dtype=np.float)
    x[n-1] = y[n-1] / u[n-1][n-1]
    for i in range(n-2, -1, -1): # from n-2 (included) to 0 (included)
        yi = y[i]
        for j in range(i+1, n):
            yi -= x[j] * u[i][j]
        x[i] = yi / u[i][i]