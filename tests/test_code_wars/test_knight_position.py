import pytest

from src.code_problems.code_wars.kyu_7.knight_position import possible_positions


@pytest.mark.parametrize('pos,expected', [
    ('a1', ['b3', 'c2']),
])
@pytest.mark.parametrize('function', [possible_positions])
def test_knight_position(pos, expected, function):
    result = function(pos)
    assert result == expected
