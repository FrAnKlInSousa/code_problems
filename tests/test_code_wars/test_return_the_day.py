import pytest

from src.code_problems.code_wars.kyu_8.return_the_day import what_day, what_day_alternative


@pytest.mark.parametrize('number,expected', [
    (1, "Sunday"),
    (2, "Monday"),
    (3, "Tuesday"),
    (4, "Wednesday"),
    (5, "Thursday"),
    (6, "Friday"),
    (7, "Saturday"),
    (8, "Wrong, please enter a number between 1 and 7")
])
@pytest.mark.parametrize('function', [what_day, what_day_alternative])
def test_what_day(number, expected, function):
    assert function(number) == expected