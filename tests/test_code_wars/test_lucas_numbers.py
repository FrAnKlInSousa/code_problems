import pytest

from src.code_problems.code_wars.kyu_6.lucas_numbers import lucas_num


@pytest.mark.parametrize('num,expected', [
    (0, 2),
    (5, 11),
    (-1, -1),
    (-10, 123),
    (10, 123),
    (-2, 3),
    (-4, 7),
    (-6, 18),
    (100, 792070839848372253127),
    (790, 1259609123094719610696679508622028645593973044347360698664403045421693635587151127607313268149509797820403345957069198184348565289422849125197626867092866282355155123)
])
@pytest.mark.parametrize('function', [lucas_num])
def test_lucas_numbers(num, expected, function):
    result = function(num)
    assert result == expected
