from math import isqrt

# https://www.codewars.com/kata/5592e3bd57b64d00f3000047/python


def pile_of_cubes(number: int) -> int:
    sqrt_number = isqrt(number)
    if sqrt_number**2 != number:  # Verificando se é um quadrado perfeito
        return -1
    n = 1
    soma = 0
    while soma < number:
        soma += n**3
        n += 1
    return n - 1 if soma == number else -1
