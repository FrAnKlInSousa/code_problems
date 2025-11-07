import pytest

from src.code_problems.code_wars.kyu_6.tribonacci_sequence import tribonacci, tribonacci_clever


@pytest.mark.parametrize('signature,number,expected', [
    ([1, 1, 1], 10, [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]),
    ([0, 0, 1], 10, [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]),
    ([0, 1, 1], 10, [0, 1, 1, 2, 4, 7, 13, 24, 44, 81]),
    ([1, 0, 0], 10, [1, 0, 0, 1, 1, 2, 4, 7, 13, 24]),
    ([0, 0, 0], 10, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    ([1, 2, 3], 10, [1, 2, 3, 6, 11, 20, 37, 68, 125, 230]),
    ([3, 2, 1], 10, [3, 2, 1, 6, 9, 16, 31, 56, 103, 190]),
    ([1, 1, 1], 1, [1]),
    ([300, 200, 100], 0, []),
    ([0.5, 0.5, 0.5], 30, [0.5, 0.5, 0.5, 1.5, 2.5, 4.5, 8.5, 15.5, 28.5, 52.5, 96.5, 177.5, 326.5, 600.5, 1104.5, 2031.5, 3736.5, 6872.5, 12640.5, 23249.5, 42762.5, 78652.5, 144664.5, 266079.5, 489396.5, 900140.5, 1655616.5, 3045153.5, 5600910.5, 10301680.5]),
    ([128, 108, 189], 2, [128, 108])
])
@pytest.mark.parametrize('function', [tribonacci, tribonacci_clever])
def test_tribonacci_sequence(signature, number, expected, function):
    result = function(signature.copy(), number)
    assert result == expected
