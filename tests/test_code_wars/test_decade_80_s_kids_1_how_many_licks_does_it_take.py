import pytest
from src.code_problems.code_wars.kyu_7.decade_80_s_kids_1_how_many_licks_does_it_take import total_licks

@pytest.mark.parametrize('env,expected', [
    ({"freezing temps": 10, "clear skies": -2},
    "It took 260 licks to get to the tootsie roll center of a tootsie pop. The toughest challenge was freezing temps."),
    ({"happiness": -5, "clear skies": -2},
    "It took 245 licks to get to the tootsie roll center of a tootsie pop."),
    ({},
    "It took 252 licks to get to the tootsie roll center of a tootsie pop."),
    ({"dragons": 100, "evil wizards": 110, "trolls": 50},
    "It took 512 licks to get to the tootsie roll center of a tootsie pop. The toughest challenge was evil wizards."),
    ({"white magic": -250},
    "It took 2 licks to get to the tootsie roll center of a tootsie pop."),
])
@pytest.mark.parametrize('function', [total_licks])
def test_80_s_kids_1_how_many_licks_does_it_take(env, expected, function):
    result = function(env)
    assert result == expected
