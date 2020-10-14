from sympy import *

a = Symbol("a")
x1 = Symbol("x1")
x2 = Symbol("x2")


def solve_test(e):
    r = solve(e, [x1, x2])

    for n in [0.99, 0.991]:
        print(f"a={n}")
        for k in r:
            print(f"{k}: {r[k].subs(a, n)}")
        print("---")


print("(1)")
solve_test([
    x1 + a * x2 - 1,
    a * x1 + x2,
])

print("\n(2)")
solve_test([
    x1 + a * x2 - 1,
    a * x1 + 4 * x2,
])
