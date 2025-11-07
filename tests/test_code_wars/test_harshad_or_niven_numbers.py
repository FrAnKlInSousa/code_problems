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


@pytest.mark.parametrize('number,expected', [
    (10, [1,2,3,4,5,6,7,8,9,10]),
    (20, [1,2,3,4,5,6,7,8,9,10,12,18,20,21,24,27,30,36,40,42]),
])
def test_get_harshad_series(number, expected):
    assert harshad.get_series(number) == expected


@pytest.mark.parametrize('number,start,expected', [
    (10, 1000, [1002, 1008, 1010, 1011, 1012, 1014, 1015, 1016, 1017, 1020])
])
def test_get_harshad_series_with_optional_start(number, start, expected):
    assert harshad.get_series(number, start=start) == expected
