import pytest

from src.code_problems.code_wars.kyu_8.removing_elements import remove_every_other


@pytest.mark.parametrize('elements,expected', [
    (["Keep", "Remove", "Keep", "Remove", "Keep"], ["Keep", "Keep", "Keep"]),
    (['Hello', 'Goodbye', 'Hello Again'], ['Hello', 'Hello Again']),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 5, 7, 9]),
    ([[1, 2]], [[1, 2]])
])
@pytest.mark.parametrize('function', [remove_every_other])
def test_removing_elements(elements, expected, function):
    result = function(elements)
    assert result == expected
