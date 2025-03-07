import pytest

@pytest.mark.parametrize(',expected', [
    (),
])
@pytest.mark.parametrize('function', [])
def test_pete_the_baker(expected, function):
    result = function()
    assert result == expected