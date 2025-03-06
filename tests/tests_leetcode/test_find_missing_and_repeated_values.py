import pytest

from src.code_problems.leetcode.easy.find_missing_and_repeated_values import find_values, find_values_alternative


@pytest.mark.parametrize('grid,expected', [
    ([[1,3],[2,2]], [2,4]),
    ([[9,1,7],[8,9,2],[3,4,6]], [9,5])
])
@pytest.mark.parametrize('function', [
    find_values, find_values_alternative])
def test_find_missing_and_repeated_values(function, grid, expected):
    result = function(grid)
    assert result == expected
