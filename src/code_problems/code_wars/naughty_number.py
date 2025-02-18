import copy
from typing import Any, List

# https://www.codewars.com/kata/679bdbe30a5faf7bbf634e0f


def is_empty(sub_arr) -> bool:
    return len(sub_arr) == 0


def arr_has_number(sub_arr) -> bool:
    int_type = type(1)

    if len(sub_arr) > 0:
        return type(sub_arr[0]) is int_type
    return False


def naughty_number(arr: List[List]) -> int:
    for idx, item in enumerate(arr):
        # vazio
        if len(item) == 0:
            continue

        item_copy = copy.deepcopy(item)

        while item_copy:
            # achou o numero
            if isinstance(item_copy, int):
                return idx
            if len(item_copy) > 0:
                item_copy = item_copy.pop()


def naughty_number_clever(arr: List[List]) -> int:
    str_arr = str(arr)
    filter_arr = [char for char in str_arr if char == ',' or char.isdigit()]
    for idx, char in enumerate(filter_arr):
        if char != ',':
            return idx


def naughty_number_gpt(arr: List[List]) -> int:
    def find_number(subarr: Any) -> bool:
        if isinstance(subarr, int):
            return True
        if isinstance(subarr, list):
            return any(find_number(item) for item in subarr)
        return False

    for idx, sublist in enumerate(arr):
        if find_number(sublist):
            return idx

    return -1
