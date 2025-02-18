import pytest

from src.code_problems.code_wars.who_is_paying import who_is_paying


@pytest.mark.parametrize(
    'name, expected',
    [
        ('Mexico', ['Mexico', 'Me']),
        ('Melania', ['Melania', 'Me']),
        ('Melissa', ['Melissa', 'Me']),
        ('Me', ['Me']),
        ('', ['']),
        ('I', ['I']),
    ],
)
def test_who_is_paying(name, expected):
    result = who_is_paying(name)
    assert result == expected
