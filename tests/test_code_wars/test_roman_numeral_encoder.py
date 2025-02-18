import pytest

from src.code_problems.code_wars.roman_numeral_encoder import (
    roman_numeral_encoder,
    roman_numeral_encoder_gpt,
)


@pytest.mark.parametrize(
    'number,expected',
    [
        (1, 'I'),
        (1000, 'M'),
        (1666, 'MDCLXVI'),
        (4, 'IV'),
        (6, 'VI'),
        (14, 'XIV'),
        (21, 'XXI'),
        (89, 'LXXXIX'),
        (91, 'XCI'),
        (984, 'CMLXXXIV'),
        (1000, 'M'),
        (1889, 'MDCCCLXXXIX'),
        (1989, 'MCMLXXXIX'),
    ],
)
@pytest.mark.parametrize(
    'function', [roman_numeral_encoder, roman_numeral_encoder_gpt]
)
def test_roman_numeral_encoder(number, expected, function):
    result = roman_numeral_encoder_gpt(number)
    assert result == expected
