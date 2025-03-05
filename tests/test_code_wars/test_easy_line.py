import pytest

from src.code_problems.code_wars.kyu_7.easy_line import easy_line, easy_line_clever


@pytest.mark.parametrize('line_number,expected', [
    (0, 1),
    (1, 2),
    (4, 70),
    (7, 3432),
    (13, 10400600),
    (17, 2333606220),
    (19, 35345263800),
    (50, 100891344545564193334812497256),
])
@pytest.mark.parametrize('function', [easy_line, easy_line_clever])
def test_easy_line(line_number, expected, function):
    result = function(line_number)
    assert result == expected