import pytest

from src.code_problems.code_wars.kyu_7.boolean_logic_from_scratch import func_or, func_xor, func_or_clever, \
    func_xor_clever, func_xor_clever_2


@pytest.mark.parametrize('a,b,expected', [
    (True, True, True),
    (True, False, True),
    (False, False, False),
    (0, 11, True),
    (None, [], False),
])
@pytest.mark.parametrize('function', [func_or, func_or_clever])
def test_boolean_logic_from_scratch_or(a, b, expected, function):
    result = function(a, b)
    assert result == expected


@pytest.mark.parametrize('a,b,expected', [
    (True, True, False),
    (True, False, True),
    (False, False, False),
    (0, 11, True),
    (None, [], False)
])
@pytest.mark.parametrize('function', [func_xor, func_xor_clever, func_xor_clever_2])
def test_boolean_logic_from_scratch_xor(a, b, expected, function):
    result = function(a, b)
    assert result == expected