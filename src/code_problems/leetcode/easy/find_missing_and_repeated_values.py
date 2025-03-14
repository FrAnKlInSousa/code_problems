from typing import List


def find_values(grid: List[List[int]]) -> List[int]:
    missing = list(range(1, (len(grid) ** 2) + 1))
    duplicated = set()
    repeated = None
    for line in grid:
        for cel in line:
            if cel in missing:
                missing.remove(cel)
            if cel in duplicated:
                repeated = cel
            else:
                duplicated.add(cel)
    return [repeated, missing[0]]


def find_values_alternative(grid: List[List[int]]) -> List[int]:
    values_to_check = set(range(1, (len(grid) ** 2) + 1))
    matrix_values = set()
    duplicated = set()
    repeated = None
    for line in grid:
        for cel in line:
            matrix_values.add(cel)
            if cel in duplicated:
                repeated = cel
            else:
                duplicated.add(cel)
    missing = values_to_check.difference(matrix_values).pop()
    return [repeated, missing]
