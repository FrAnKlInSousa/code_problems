"""
https://www.codewars.com/kata/54c27a33fb7da0db0100040e
"""


def you_are_square(number) -> bool:
    if number < 0:
        return False
    sqr = int(number ** (1 / 2))
    return sqr * sqr == number
