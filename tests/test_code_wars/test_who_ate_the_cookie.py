import pytest

from src.code_problems.code_wars.kyu_8.who_ate_the_cookie import cookie


@pytest.mark.parametrize('data,expected', [
    ('Ryan', 'Who ate the last cookie? It was Zach!'),
    (2.3, 'Who ate the last cookie? It was Monica!'),
    (26, 'Who ate the last cookie? It was Monica!'),
    (True, 'Who ate the last cookie? It was the dog!'),
])
@pytest.mark.parametrize('function', [cookie])
def test_who_ate_the_cookie(data, expected, function):
    result = function(data)
    assert result == expected
