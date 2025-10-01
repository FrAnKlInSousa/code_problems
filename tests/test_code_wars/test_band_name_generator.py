import pytest

from src.code_problems.code_wars.kyu_7.band_name_generator import band_name_generator


@pytest.mark.parametrize('name,expected', [
    ("knife", "The Knife"),
    ("tart", "Tartart"),
    ("sandles", "Sandlesandles"),
    ("bed", "The Bed"),
    ("qq", "Qqq"),
])
@pytest.mark.parametrize('function', [band_name_generator])
def test_band_name_generator(name, expected, function):
    result = function(name)
    assert result == expected
