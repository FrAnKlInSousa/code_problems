import pytest

from src.code_problems.code_wars.kyu_7.factorial import factorial, recursive_factorial


@pytest.mark.parametrize('number,expected', [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6)
])
@pytest.mark.parametrize('function', [factorial, recursive_factorial])
def test_factorial(number, expected, function):
    result = function(number)
    assert result == expected

@pytest.mark.parametrize('number', [-1, 13])
@pytest.mark.parametrize('function', [factorial, recursive_factorial])
def test_factorial_error(number, function):
    with pytest.raises(ValueError):
        function(number)