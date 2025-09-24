"""
https://www.codewars.com/kata/54da5a58ea159efa38000836
"""

from typing import List


def find_the_odd(numbers: List[int]) -> int | None:
    count_numbers = {}
    for num in numbers:
        if num not in count_numbers:
            count_numbers.update({num: 1})
        else:
            count_numbers.update({num: count_numbers.get(num) + 1})
    for k, v in count_numbers.items():
        if v % 2 != 0:
            return k


def find_the_odd_alternative(numbers: List[int]) -> int:
    for number in numbers:
        if numbers.count(number) % 2 != 0:
            return number
