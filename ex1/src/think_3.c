#include <stdio.h>
#define TOL 1e-5

// double 的 abs
double absd(double a) { return a >= 0 ? a : -a; }

// iter 从 x_0 = x0 开始，做 x_{k+1} = f(x_k, a) 的迭代
// 直到 abs((x_k - x_{k-1}) / x_k) < tol
double iter(double (*f)(double xk, double a), double a, double x0, double tol) {
    double xk_prev;
    double xk = x0;

    int count = 0;

    do {
        xk_prev = xk;
        xk = f(xk, a);
        count++;
    } while (absd((xk - xk_prev) / xk) >= tol);

    printf("a: %f\t x0: %f\t iter_times: %d\t result: %f\n", a, x0, count, xk);
    return xk;
}

// 迭代函数
double f(double xk, double a) { return (xk + a / xk) / 2.0; }

int main() {
    double a = 9;

    iter(f, a, 1, TOL);
    iter(f, a, 2, TOL);
    iter(f, a, 2.5, TOL);
    iter(f, a, 3, TOL);
    iter(f, a, 3.5, TOL);
    iter(f, a, 4, TOL);
    iter(f, a, 100, TOL);

    return 0;
}