import pytest

from src.code_problems.code_wars.kyu_6.fibonacci_tribonacci_and_friends import xbonacci


@pytest.mark.parametrize('signature,size,expected', [
    ([0, 1], 10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
    ([1, 1], 10, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]),
    ([0, 0, 0, 0, 1], 10, [0, 0, 0, 0, 1, 1, 2, 4, 8, 16]),
    ([1, 0, 0, 0, 0, 0, 1], 10, [1, 0, 0, 0, 0, 0, 1, 2, 3, 6]),
    ([1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 20, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 4, 8, 16, 32, 64, 128, 256]),
    ([0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0], 10, [0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    ([0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0], 20, [0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0.5, 1, 2, 4, 8, 16, 32, 64, 128]),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 20, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 9, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 0, [])
])
@pytest.mark.parametrize('function', [xbonacci])
def test_fibonacci_tribonacci_and_friends(signature, size, expected, function):
    result = function(signature.copy(), size)
    assert result == expected
