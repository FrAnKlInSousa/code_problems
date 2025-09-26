import pytest

from src.code_problems.code_wars.kyu_8.convert_number_to_reversed_array_of_digits import invert_number


@pytest.mark.parametrize('number,expected', [
    (35231, [1,3,2,5,3]),
    (0,[0]),
    (23582357,[7,5,3,2,8,5,3,2]),
    (984764738,[8,3,7,4,6,7,4,8,9]),
    (45762893920,[0,2,9,3,9,8,2,6,7,5,4]),
    (548702838394,[4,9,3,8,3,8,2,0,7,8,4,5]),
])
@pytest.mark.parametrize('function', [invert_number])
def test_convert_number_to_reversed_array_of_digits(number, expected, function):
    result = function(number)
    assert result == expected
