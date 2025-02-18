import pytest

from src.code_problems.code_wars.exclamation_marks_series import (
    change_to_exclamation_mark, change_to_exclamation_mark_regex,
)


@pytest.mark.parametrize(
    'text,expected',
    [
        ('Hi!', 'H!!'),
        ('!Hi! Hi!', '!H!! H!!'),
        ('aeiou', '!!!!!'),
        ('ABCDE', '!BCD!'),
    ],
)
@pytest.mark.parametrize('function', [change_to_exclamation_mark, change_to_exclamation_mark_regex])
def test_change_to_exclamation_marks(text, expected, function):
    result = function(text)
    assert result == expected
