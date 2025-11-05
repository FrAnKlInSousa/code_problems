import pytest

from src.code_problems.code_wars.kyu_6.harshad_or_niven_numbers import Harshad

harshad = Harshad()

@pytest.mark.parametrize('number', [
    10, 27, 588
])
def test_harshad_valid_numbers(number):
    assert harshad.is_valid(number)


@pytest.mark.parametrize('number', [
    19, 589, 1001
])
def test_harshad_invalid_numbers(number):
    assert not harshad.is_valid(number)