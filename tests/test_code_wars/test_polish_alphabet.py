import pytest

from src.code_problems.code_wars.polish_alphabet import (
    polish,
    polish_alternative,
)


@pytest.mark.parametrize(
    'word,expected',
    [
        ('Jędrzej Błądziński', 'Jedrzej Bladzinski'),
        ('Lech Wałęsa', 'Lech Walesa'),
        ('Maria Skłodowska-Curie', 'Maria Sklodowska-Curie'),
    ],
)
@pytest.mark.parametrize('function', [polish, polish_alternative])
def test_polish_alphabet(word, expected, function):
    result = function(word)
    assert result == expected
