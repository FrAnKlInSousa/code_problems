import pytest

from src.code_problems.code_wars.kyu_7.red_knight import red_knight, red_knight_clever, red_knight_clever_2


@pytest.mark.parametrize('knight,pawn,expected', [
    (0, 8, ('White', 16)),
    (0, 7, ('Black', 14)),
    (1, 6, ('Black', 12)),
    (1, 5, ('White', 10)),
])
@pytest.mark.parametrize('function', [red_knight, red_knight_clever, red_knight_clever_2])
def test_red_knight(knight, pawn, expected, function):
    result = function(knight, pawn)
    assert result == expected
