import pytest

from src.code_problems.code_wars.kyu_8.is_the_string_uppercase import is_uppercase


@pytest.mark.parametrize('string,expected', [
    ('c', False),
    ('C', True),
    ('hello I AM DONALD', False),
    ('HELLO I AM DONALD', True),
    ('$%&', True),
])
@pytest.mark.parametrize('function', [is_uppercase])
def test_is_the_string_uppercase(string, expected, function):
    result = function(string)
    assert result == expected
