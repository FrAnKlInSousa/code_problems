import pytest

from src.code_problems.code_wars.array_diff import (
    array_diff,
    array_diff_clever,
)


@pytest.mark.parametrize(
    'array_a,array_b,expected',
    [
        ([1, 2], [1], [2]),
        ([1, 2, 2], [1], [2, 2]),
        ([1, 2, 2], [2], [1]),
        ([1, 2, 2], [], [1, 2, 2]),
        ([], [1, 2], []),
        ([1, 2, 3], [1, 2], [3]),
    ],
)
@pytest.mark.parametrize('function', [array_diff, array_diff_clever])
def test_array_diff(array_a, array_b, expected, function):
    result = function(array_a, array_b)
    assert result == expected
