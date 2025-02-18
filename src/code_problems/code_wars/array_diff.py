from typing import List


# https://www.codewars.com/kata/523f5d21c841566fde000009/
def array_diff(array_a: List, array_b: List) -> List:
    for item_b in array_b:
        while item_b in array_a:
            array_a.remove(item_b)
    return array_a


def array_diff_clever(array_a: List, array_b: List) -> List:
    return [item for item in array_a if item not in array_b]
