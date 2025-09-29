import pytest

from src.code_problems.code_wars.kyu_7.find_the_area_of_the_rectangle import area


@pytest.mark.parametrize('diagonal,side,expected', [
    (5, 4, 12),
    (10, 6, 48),
    (13, 5, 60),
    (12, 5, 54.54),
    (5, 5, "Not a rectangle"),
    (3, 5, "Not a rectangle")])
@pytest.mark.parametrize('function', [area])
def test_find_the_area_of_the_rectangle(diagonal, side, expected, function):
    result = function(diagonal, side)
    assert result == expected
