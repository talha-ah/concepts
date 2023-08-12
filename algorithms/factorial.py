import math


def fact(n):
    if n < 0:
        raise ValueError("factorial() not defined for negative values")

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


def fact_recur(n):
    if n < 0:
        raise ValueError("factorial() not defined for negative values")

    if n < 2:
        return 1

    return n * fact_recur(n - 1)


print(fact(23))
print(fact_recur(23))
print(math.factorial(23))
