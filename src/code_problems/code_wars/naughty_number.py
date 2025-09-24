import copy
from typing import List


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
