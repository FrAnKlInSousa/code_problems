from math import isqrt

# https://www.codewars.com/kata/5592e3bd57b64d00f3000047/python


def pile_of_cubes(number: int) -> int:
    n = 1
    soma = 0
    while soma < number:
        soma += n**3
        n += 1
    return n - 1 if soma == number else -1


def pile_of_cubes_clever(number: int) -> int:
    sqrt_number = isqrt(number)
    if sqrt_number**2 != number:  # Verificando se é um quadrado perfeito
        return -1

    # Resolvendo a equação quadrática n^2 + n - 2 * sqrt_number = 0
    a, b, c = 1, 1, -2 * sqrt_number

    delta = b**2 - 4 * a * c
    if delta < 0:
        return -1

    sqrt_delta = isqrt(delta)
    if sqrt_delta**2 != delta:
        return -1

    # Calculando as raízes
    x1 = (-b + sqrt_delta) // (2 * a)
    x2 = (-b - sqrt_delta) // (2 * a)

    if x1 >= 0:
        return x1
    if x2 >= 0:
        return x2
    return -1
