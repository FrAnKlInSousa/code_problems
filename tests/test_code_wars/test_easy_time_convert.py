import pytest

from src.code_problems.code_wars.kyu_7.easy_time_convert import time_convert, time_convert_clever


@pytest.mark.parametrize('num,expected', [
(0, '00:00'),
        (-6, '00:00'),
        (8, '00:08'),
        (32, '00:32'),
        (75, '01:15'),
        (63, '01:03'),
        (134, '02:14'),
        (180, '03:00'),
        (970, '16:10'),
        (565757, '9429:17'),
])
@pytest.mark.parametrize('function', [time_convert, time_convert_clever])
def test_easy_time_convert(num, expected, function):
    result = function(num)
    assert result == expected
