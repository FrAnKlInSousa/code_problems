import pytest

from src.code_problems.code_wars.simple_pig_latin import (
    simple_pig_latin,
    simple_pig_latin_gpt,
)


@pytest.mark.parametrize(
    'phrase,expected',
    [
        ('Pig latin is cool', 'igPay atinlay siay oolcay'),
        ('This is my string', 'hisTay siay ymay tringsay'),
        ('O tempora o mores !', 'Oay emporatay oay oresmay !'),
    ],
)
@pytest.mark.parametrize('function', [simple_pig_latin, simple_pig_latin_gpt])
def test_simple_pig_latin(phrase, expected, function):
    result = function(phrase)
    assert result == expected
