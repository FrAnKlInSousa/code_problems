import pytest

from src.code_problems.code_wars.kyu_5.pete_the_baker import pete_the_baker


@pytest.mark.parametrize('recipe,ingredients,expected', [
    ({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}, 2),
    ({'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}, {'sugar': 500, 'flour': 2000, 'milk': 2000}, 0)
])
@pytest.mark.parametrize('function', [pete_the_baker])
def test_pete_the_baker(expected, function, recipe, ingredients):
    result = function(recipe, ingredients)
    assert result == expected
