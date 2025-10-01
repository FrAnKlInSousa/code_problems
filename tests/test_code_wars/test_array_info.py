import pytest

from src.code_problems.code_wars.kyu_7.array_info import array_info, array_info_clever


@pytest.mark.parametrize('array,expected', [
    ([1, 2, 3.33, 4, 5.01, 'bass', 'kick', ' '], [[8], [3], [2], [2], [1]]),
    ([0.001, 2, ' '], [[3], [1], [1], [None], [1]]),
    ([], 'Nothing in the array!'),
    ([' '], [[1], [None], [None], [None], [1]]),
    ([0.001, 2, 'bass'], [[3], [1], [1], [1], [None]])
])
@pytest.mark.parametrize('function', [array_info, array_info_clever])
def test_array_info(array, expected, function):
    result = function(array)
    assert result == expected
