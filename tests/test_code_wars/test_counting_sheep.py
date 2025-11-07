import pytest

from src.code_problems.code_wars.kyu_8.counting_sheep import count_sheeps


@pytest.mark.parametrize('sheeps,expected', [
    ([True,  True,  True,  False,
      True,  True,  True,  True ,
      True,  False, True,  False,
      True,  False, False, True ,
      True,  True,  True,  True ,
      False, False, True,  True ], 17),
    ([], 0)
])
@pytest.mark.parametrize('function', [count_sheeps])
def test_counting_sheep(sheeps, expected, function):
    result = function(sheeps)
    assert result == expected
