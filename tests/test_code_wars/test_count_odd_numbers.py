import pytest

from src.code_problems.code_wars.count_odd_numbers import count_odd_numbers


@pytest.mark.parametrize('number,expected', [(7, 3), (15, 7), (15023, 7511)])
def test_count_odd(number, expected):
    result = count_odd_numbers(number)
    assert result == expected
