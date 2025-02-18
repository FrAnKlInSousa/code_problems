import pytest

from src.code_problems.code_wars.you_are_square import you_are_square


@pytest.mark.parametrize(
    'number,expected',
    [(-1, False), (0, True), (3, False), (4, True), (25, True), (26, False)],
)
def test_you_are_square(number, expected):
    result = you_are_square(number)
    assert result == expected
