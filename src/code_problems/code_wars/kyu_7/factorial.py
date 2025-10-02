def factorial(n):
    if n > 12 or n < 0:  # noqa PLR2004
        raise ValueError()
    elif n == 0:
        return 1
    fact = 1
    while n > 1:
        fact *= n
        n -= 1
    return fact


def recursive_factorial(n):
    if 0 > n or n > 12:  # noqa PLR2004
        raise ValueError
    if n == 0:
        return 1
    return n * recursive_factorial(n - 1)
