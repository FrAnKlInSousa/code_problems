import pytest

from src.code_problems.code_wars.kyu_7.most_digits import find_longest


@pytest.mark.parametrize('arr,expected', [
    ([1, 10, 100], 100),
    ([9000, 8, 800], 9000),
    ([8, 900, 500], 900),
    ([3, 40000, 100], 40000),
    ([1, 200, 100000], 100000),
    ([1, 399, 400], 399)
])
@pytest.mark.parametrize('function', [find_longest])
def test_most_digits(arr, expected, function):
    result = function(arr)
    assert result == expected
