from typing import List


def unique_sets(group: List[set]) -> bool:
    found_values = set()

    def has_duplicated_value(my_set_list, scanner: set) -> bool:
        for sub_item in my_set_list:
            if isinstance(sub_item, tuple):
                if not has_duplicated_value(sub_item, found_values):
                    continue
                return True
            if isinstance(sub_item, (set, frozenset)):
                if not has_duplicated_value(frozenset(sub_item), found_values):
                    continue
                return True
            if sub_item in scanner:
                return True
            scanner.add(sub_item)
        return False

    for item in group:
        if has_duplicated_value(item, found_values):
            return False
    return True
