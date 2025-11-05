import pytest

from src.code_problems.code_wars.kyu_6.harshad_or_niven_numbers import Harshad

harshad = Harshad()

@pytest.mark.parametrize('number', [
    0, 10, 27, 588
])
def test_harshad_valid_numbers(number):
    assert harshad.is_valid(number)


@pytest.mark.parametrize('number', [
    19, 589, 1001
])
def test_harshad_invalid_numbers(number):
    assert not harshad.is_valid(number)


@pytest.mark.parametrize('number,expected', [
    (0, 1),
    (1, 2),
    (17, 18),
    (25, 27)
])
def test_next_harshad_numbers(number, expected):
    assert harshad.get_next(number) == expected
