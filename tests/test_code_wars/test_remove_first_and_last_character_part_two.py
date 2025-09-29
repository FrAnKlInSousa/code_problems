import pytest

from src.code_problems.code_wars.kyu_8.remove_first_and_last_character_part_two import array


@pytest.mark.parametrize('string,expected', [
    ('1,2,3', '2'),
    ('1,2,3,4', '2 3'),
    ('1,2,3,4,5', '2 3 4'),
    ('', None),
    ('1', None),
    ('1,2', None)
])
@pytest.mark.parametrize('function', [array])
def test_remove_first_and_last_character_part_two(string, expected, function):
    result = function(string)
    assert result == expected
