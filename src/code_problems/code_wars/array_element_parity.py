"""
https://www.codewars.com/kata/5a092d9e46d843b9db000064
"""

from typing import List


def array_element_parity(numbers: List[int]) -> int | None:
    def has_oposite(candidate: int) -> bool:
        return candidate - (2 * candidate) in numbers

    for number in numbers:
        if not has_oposite(number):
            return number


def array_element_parity_clever(numbers: List[int]) -> int | None:
    return sum(set(numbers))
