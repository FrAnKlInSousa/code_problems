import pytest

from src.code_problems.code_wars.kyu_8.ensure_question import ensure_question


@pytest.mark.parametrize('phrase,expected', [
    ('', '?'),
    ('Yes', 'Yes?'),
    ('No', 'No?'),
    ('Well????', 'Well????'),
])
@pytest.mark.parametrize('function', [ensure_question])
def test_ensure_question(phrase, expected, function):
    result = function(phrase)
    assert result == expected
