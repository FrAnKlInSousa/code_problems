import pytest

from src.code_problems.code_wars.unique_in_order import (
    unique_in_order,
    unique_in_order_alternative,
)


@pytest.mark.parametrize(
    'sequence,expected',
    [
        ('AAAABBBCCDAABBB', ['A', 'B', 'C', 'D', 'A', 'B']),
        ('ABBCcAD', ['A', 'B', 'C', 'c', 'A', 'D']),
        ([1, 2, 2, 3, 3], [1, 2, 3]),
        ((1, 2, 2, 3, 3), [1, 2, 3]),
    ],
)
@pytest.mark.parametrize(
    'function', [unique_in_order, unique_in_order_alternative]
)
def test_unique_in_order(sequence, expected, function):
    result = function(sequence)
    assert result == expected
