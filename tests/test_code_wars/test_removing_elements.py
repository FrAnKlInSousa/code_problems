import pytest


@pytest.mark.parametrize(',expected', [
    (),
])
@pytest.mark.parametrize('function', [])
def test_removing_elements(expected, function):
    result = function()
    assert result == expected
