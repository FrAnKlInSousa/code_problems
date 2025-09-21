import pytest

@pytest.mark.parametrize(',expected', [
    (),
])
@pytest.mark.parametrize('function', [])
def test_generating_numbers_from_digits_1(expected, function):
    result = function()
    assert result == expected