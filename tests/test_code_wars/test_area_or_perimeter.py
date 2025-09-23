import pytest

from src.code_problems.code_wars.kyu_8.area_or_perimeter import area_perimeter


@pytest.mark.parametrize('side_a,side_b,expected', [
    (4, 4, 16),
    (6, 10, 32)
])
@pytest.mark.parametrize('function', [area_perimeter])
def test_area_or_perimeter(side_a, side_b, expected, function):
    result = function(side_a, side_b)
    assert result == expected
