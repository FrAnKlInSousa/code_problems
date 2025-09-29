import pytest

from src.code_problems.code_wars.kyu_6.find_the_odd_int import (
    find_the_odd,
    find_the_odd_alternative,
)


@pytest.mark.parametrize(
    'number,expected',
    [
        ([7], 7),
        ([0], 0),
        ([1, 1, 2], 2),
        ([0, 1, 0, 1, 0], 0),
        ([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1], 4),
    ],
)
@pytest.mark.parametrize('function', [find_the_odd_alternative, find_the_odd])
def test_find_the_odd(number, expected, function):
    result = function(number)
    assert result == expected
