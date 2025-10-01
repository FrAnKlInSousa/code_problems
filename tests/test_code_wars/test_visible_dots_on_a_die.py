import pytest

from src.code_problems.code_wars.kyu_7.visible_dots_on_a_die import total_amount_visible


@pytest.mark.parametrize('top_num,sides,expected', [
    (3, 6, 17),
    (3, 8, 30),
    (1, 12, 66),
    (1, 6, 15),
    (6, 6, 20),
    # (9, 8, 36) #todo invalid case, but required in codewars test
])
@pytest.mark.parametrize('function', [total_amount_visible])
def test_visible_dots_on_a_die(top_num, sides, expected, function):
    result = function(top_num, sides)
    assert result == expected
