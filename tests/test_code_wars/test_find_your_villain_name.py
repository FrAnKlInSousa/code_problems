import pytest

@pytest.mark.parametrize(',expected', [
    (),
])
@pytest.mark.parametrize('function', [])
def test_find_your_villain_name(expected, function):
    result = function()
    assert result == expected