"""
https://www.codewars.com/kata/5a946d9fba1bb5135100007c
"""

from typing import List

MAX_PRIME_DIVISORS = 2


def transform_to_prime(numbers: List[int]) -> int:
    sum_numbers = sum(numbers)

    def is_prime(prime_candidate: int) -> bool:
        # tem a lib gmpy2 que faz isso e tem diversas
        # outras funções interessantes
        count = 1
        for divisor in list(range(2, prime_candidate + 1)):
            if prime_candidate % divisor == 0:
                count += 1
            if count > MAX_PRIME_DIVISORS:
                return False
        return True

    minimum_int = 0
    while not is_prime(sum_numbers):
        minimum_int += 1
        sum_numbers += 1
    return minimum_int
