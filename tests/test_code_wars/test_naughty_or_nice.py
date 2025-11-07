import pytest

from src.code_problems.code_wars.kyu_7.naughty_or_nice import what_list_am_i_on


@pytest.mark.parametrize('actions,expected', [
    (['broke someone\'s window', 'fought over a toaster', 'killed a bug'], 'naughty'),
    (['got someone a new car', 'saved a man from drowning', 'never got into a fight'], 'nice'),
    (['broke a vending machine', 'never got into a fight', 'tied someone\'s shoes'], 'naughty')
])
@pytest.mark.parametrize('function', [what_list_am_i_on])
def test_naughty_or_nice(actions, expected, function):
    result = function(actions)
    assert result == expected
