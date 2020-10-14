#include <stdio.h>
#define NUM_1 0.1234567890123456789

void float_double() {
    float ff = NUM_1;
    double df = NUM_1;

    printf("ff: %.32f\ndf: %.32f\n", ff, df);
}

// 将100个a3逐个加到a1上，返回a1
float a1_add_100a3_way1(float a1, float a3) {
    for (int i = 0; i < 100; i++) {
        a1 += a3;
    }
    return a1;
}

// 先将100个a3相加，再加到a1上，返回a1
float a1_add_100a3_way2(float a1, float a3) {
    float tmp = 0;
    for (int i = 0; i < 100; i++) {
        tmp += a3;
    }
    a1 += tmp;
    return a1;
}

void float_calc() {
    float a1 = 1.000001;
    float a2 = 1.000000;
    float a3 = 0.0000001;

    puts("1) 两种算法计算a1与100个a3相加的结果");
    float result[2];

    result[0] = a1_add_100a3_way1(a1, a3);
    result[1] = a1_add_100a3_way2(a1, a3);

    printf("方法1: %.32f\n方法2: %.32f\n", *result, *(result + 1));

    puts("2) 计算 a1/a3+a2");
    float result_add = a1 / a3 + a2;
    printf("result: %.32f\n", result_add);

    puts("计算a1-a2");
    float result_sub = a1 - a2;
    printf("result: %.32f\n", result_sub);
}

int main() {
    puts("\n1.(1)");
    float_double();

    puts("\n1.(2)");
    float_calc();

    return 0;
}
