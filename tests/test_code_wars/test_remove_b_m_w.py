import pytest

from src.code_problems.code_wars.kyu_7.remove_b_m_w import remove_bmw, remove_bmw_clever


@pytest.mark.parametrize('string,expected', [
    ('bmwvolvoBMW', 'volvo'),
    ('blablahblah', 'lalahlah')
])
@pytest.mark.parametrize('function', [remove_bmw, remove_bmw_clever])
def test_remove_b_m_w(string, expected, function):
    result = function(string)
    assert result == expected

@pytest.mark.parametrize('data', [
    (2), ([]), (())
])
@pytest.mark.parametrize('function', [remove_bmw, remove_bmw_clever])
def test_remove_b_m_w_typeerror(data, function):
    with pytest.raises(TypeError):
        function(data)
