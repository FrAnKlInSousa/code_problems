import pytest

from src.code_problems.code_wars.kyu_8.grader import grader


@pytest.mark.parametrize('score,expected', [
    (1, 'A'),
    (1.01, 'F'),
    (0.20, 'F'),
    (0.70, 'C'),
    (0.80, 'B'),
    (0.90, 'A'),
    (0.60, 'D'),
    (0.50, 'F'),
    (0.00, 'F'),
    (0.67, 'D')
])
@pytest.mark.parametrize('function', [grader])
def test_grader(score, expected, function):
    result = function(score)
    assert result == expected
