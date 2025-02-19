import pytest
from src.code_problems.code_wars.kyu_8.take_the_derivative import take_the_derivative

@pytest.mark.parametrize('coefficient,exponent,expected', [
    (7, 8, "56x^7"),
    (5, 9, "45x^8")
])
def test_take_the_derivative(coefficient, exponent, expected):
    result = take_the_derivative(coefficient, exponent)
    assert result == expected