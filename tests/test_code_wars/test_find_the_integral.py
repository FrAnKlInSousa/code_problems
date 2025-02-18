import pytest

from src.code_problems.code_wars.find_the_integral import find_integral


@pytest.mark.parametrize(
    'first_term,second_term,expected',
    [
        (3, 2, '1x^3'),
        (12, 5, '2x^6'),
        (20, 1, '10x^2'),
        (40, 3, '10x^4'),
        (90, 2, '30x^3'),
    ],
)
def test_find_the_integral(first_term, second_term, expected):
    result = find_integral(first_term, second_term)
    assert expected == result
