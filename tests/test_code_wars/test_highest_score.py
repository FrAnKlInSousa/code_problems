import pytest

from src.code_problems.code_wars.highest_score import (
    highest_score,
    highest_score_clever,
    highest_score_gpt,
)


@pytest.mark.parametrize(
    'phrase,expected',
    [
        ('man i need a taxi up to ubud', 'taxi'),
        ('what time are we climbing up the volcano', 'volcano'),
        ('take me to semynak', 'semynak'),
        ('aa b', 'aa'),
        ('b aa', 'b'),
        ('bb d', 'bb'),
        ('d bb', 'd'),
        ('aaa b', 'aaa'),
    ],
)
@pytest.mark.parametrize(
    'function', [highest_score, highest_score_clever, highest_score_gpt]
)
def test_highest_score_word(phrase, expected, function):
    result = function(phrase)
    assert result == expected
