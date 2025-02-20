import pytest

from src.code_problems.code_wars.kyu_7.driving_school_series_2 import calculate_charge


@pytest.mark.parametrize('time,expected', [
    (45, 30),
    (63, 30),
    (84,40),
    (102,50),
    (273,100)
])
def test_calculate_charge(time, expected):
    result = calculate_charge(time)
    assert result == expected
