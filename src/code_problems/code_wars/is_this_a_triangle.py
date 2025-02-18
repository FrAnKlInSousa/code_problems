"""
https://www.codewars.com/kata/56606694ec01347ce800001b
"""


def is_this_a_triangle(a: int, b: int, c: int) -> bool:
    return a < b + c and b < a + c and c < a + b


def is_this_a_triangle_clever(a: int, b: int, c: int) -> bool:
    a, b, c = sorted([a, b, c])
    return c < b + a
