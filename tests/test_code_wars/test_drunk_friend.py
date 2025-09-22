import pytest

from src.code_problems.code_wars.drunk_friend import drunk_friend


@pytest.mark.parametrize(
    'phrase,expected',
    [
        ("yvvi", "beer"),
        ("Blf zoivzwb szw 10 yvvih", "You already had 10 beers"),
        ("Ovg'h hdrn rm gsv ulfmgzrm!", "Let's swim in the fountain!"),
        ("Tl slnv, blf'iv wifmp", "Go home, you're drunk"),
        ("Hfiv r xzm wzmxv lm xlk'h xzi, slow nb yvvi", "Sure i can dance on cop's car, hold my beer"),
        ("Hvv? R'n mlg gszg wifmp, r xzm hgroo gzpv nb xolgsvh luu", "See? I'm not that drunk, i can still take my clothes off"),
        ("I NK ", "R MP ")
    ],
)
@pytest.mark.parametrize('function', [drunk_friend])
def test_drunk_friend(phrase, expected, function):
    result = function(phrase)
    assert result == expected
