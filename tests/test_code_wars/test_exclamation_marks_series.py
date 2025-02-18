import pytest

from src.code_problems.code_wars.exclamation_marks_series import (
    change_to_exclamation_mark,
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
def test_change_to_exclamation_marks(text, expected):
    result = change_to_exclamation_mark(text)
    assert result == expected
