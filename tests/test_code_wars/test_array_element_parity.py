import pytest

from src.code_problems.code_wars.array_element_parity import array_element_parity, array_element_parity_clever


@pytest.mark.parametrize('numbers,expected', [
    ([1, -1, 2, -2, 3], 3),
    ([-3, 1, 2, 3, -1, -4, -2], -4),
    ([1, -1, 2, -2, 3, 3], 3),
    ([-9, -105, -9, -9, -9, -9, 105], -9),
    ([-110, 110, -38, -38, -62, 62, -38, -38, -38], -38),
])
@pytest.mark.parametrize('function', [array_element_parity, array_element_parity_clever])
def test_array_element_parity(numbers, expected, function):
    result = function(numbers)
    assert result == expected