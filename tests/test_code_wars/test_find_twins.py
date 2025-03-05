import pytest

from src.code_problems.code_wars.kyu_7.find_twins import find_twins


@pytest.mark.parametrize('citizens,expected', [
    ([2, 5, 34, 1, 22, 1], 1),
    ([2, 2, 34, 1, 22], 2),
    ([2, 5, 34, 1, 22], None),
    ([], None),
    ([5], None),
    ([8, 2], None),
    ([3, 3], 3),
    ([0, 0], 0)
])
def test_find_twins(citizens, expected):
    result = find_twins(citizens)
    assert result == expected