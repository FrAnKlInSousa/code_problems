import pytest

from src.code_problems.code_wars.kyu_6.up_and_down import arrange


@pytest.mark.parametrize('phrase,expected', [
    ('after be arrived two My so', 'be ARRIVED two AFTER my SO'),
    ("", ""),
    ("who hit retaining The That a we taken", "who RETAINING hit THAT a THE we TAKEN"),
    ("on I came up were so grandmothers", "i CAME on WERE up GRANDMOTHERS so"),
    ("way the my wall them him", "way THE my WALL him THEM"),
    ("turn know great-aunts aunt look A to back", "turn GREAT-AUNTS know AUNT a LOOK to BACK")

])
@pytest.mark.parametrize('function', [arrange])
def test_up_and_down(phrase, expected, function):
    result = function(phrase)
    assert result == expected
