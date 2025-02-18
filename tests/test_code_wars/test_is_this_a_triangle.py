import pytest

from src.code_problems.code_wars.is_this_a_triangle import (
    is_this_a_triangle,
    is_this_a_triangle_clever,
)


@pytest.mark.parametrize(
    'a,b,c,expected',
    [
        (1, 2, 2, True),
        (2, 2, 2, True),
        (1, 2, 3, False),
        (-5, 1, 3, False),
        (0, 2, 3, False),
        (1, 2, 9, False),
    ],
)
@pytest.mark.parametrize(
    'function', [is_this_a_triangle_clever, is_this_a_triangle]
)
def test_is_this_a_triangle(a, b, c, expected, function):
    result = function(a, b, c)
    assert result == expected
