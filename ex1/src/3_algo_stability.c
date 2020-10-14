#include <stdio.h>

#define I0 0.1823
#define I100 0.001815
#define TEST_COUNT 4

double algo_1(int n) {
    if (n == 0) {
        return I0;
    }

    return 1.0 / n - 5.0 * algo_1(n - 1);
}

double algo_2(int n) {
    if (n == 100) {
        return I100;
    }

    return (1.0 / n - algo_2(n + 1)) / 5.0;
}

int main() {
    int points[TEST_COUNT] = {8, 10, 12, 14};
    double accuracy[TEST_COUNT] = {0.01884, 0.01536, 0.01297, 0.01123};

    puts("algo_1: I(n) = 1 / n - 5 * I(n - 1)");
    puts("algo_2: I(n) = (1 / n - I(n + 1)) / 5\n");

    for (int i = 0; i < TEST_COUNT; i++) {
        printf("accuracy: I(%d) = %f\n", points[i], accuracy[i]);
        printf("algo_1: %f\n", algo_1(points[i]));
        printf("algo_2: %f\n\n", algo_2(points[i]));
    }
}
