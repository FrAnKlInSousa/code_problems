import pytest
from datetime import datetime


from src.code_problems.code_wars.kyu_7.find_your_villain_name import villain_name


@pytest.mark.parametrize('birthdate,expected', [
    ("1/1/2000", "The Evil Pickle"),
    ("2/2/2000", "The Vile Hood Ornament"),
    ("2/12/2000", "The Awkward Hood Ornament"),
])
@pytest.mark.parametrize('function', [villain_name])
def test_find_your_villain_name(birthdate, expected, function):
    result = function(datetime.strptime(birthdate, '%d/%m/%Y'))
    assert result == expected
