from typing import Any


def remove_every_other(my_list: list[Any]) -> list[Any]:
    new_elements = []
    for index, element in enumerate(my_list):
        if index % 2 == 0:
            new_elements.append(element)
    return new_elements


def remove_every_other_b(my_list: list[Any]) -> list[Any]:
    return my_list[::2]
