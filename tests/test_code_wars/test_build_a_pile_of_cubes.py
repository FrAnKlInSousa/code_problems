import pytest

from src.code_problems.code_wars.build_a_pile_of_cubes import (
    pile_of_cubes,
)


@pytest.mark.parametrize(
    'number,expected',
    [
        (1071225, 45),
        (91716553919377, -1),
        (4, -1),
        (16, -1),
        (4183059834009, 2022),
        (24723578342962, -1),
        (135440716410000, 4824),
        (40539911473216, 3568),
        (26825883955641, 3218),
        (6555550967576240401, -1),
    ],
)
@pytest.mark.parametrize(
    'function',
    [
        pile_of_cubes,
    ],
)
def test_pile_of_cubes(number, expected, function):
    result = function(number)
    assert result == expected
