#include <stdio.h>

// 一元可微函数 f(x) 在 x0 处导数的近似方法
double df_1(double (*f)(double), double x0, double h) {
    return (f(x0 + h) - f(x0)) / h;
}

// 一元可微函数 f(x) 在 x0 处导数的近似方法
double df_2(double (*f)(double), double x0, double h) {
    return (f(x0 + h) - f(x0 - h)) / (2 * h);
}

// f(x) = x^3
double f(double x) { return x * x * x; }

int main() {
    double x0 = 1;
    double h = 1;

    puts("f(x) = x * x * x");
    puts("df_1(f, x0, h) = (f(x0 + h) - f(x0)) / h");
    puts("df_2(f, x0, h) = (f(x0 + h) - f(x0 - h)) / (2 * h)\n");

    for (int i = 0; i < 16; i++) {
        double diff_result[2];  // 存放 df_1、df_2 的结果

        diff_result[0] = df_1(f, x0, h);
        diff_result[1] = df_2(f, x0, h);

        printf("--- h = %g ---\n", h);
        printf("df_1: %f\ndf_2: %f\n\n", *diff_result, *(diff_result + 1));

        h /= 10;
    }

    return 0;
}
