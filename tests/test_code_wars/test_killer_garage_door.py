import pytest

from src.code_problems.code_wars.kyu_6.killer_garage_door import controller
"""
alt + enter (corrigir erro/alerta)
ctrl shift arrow up/down
ctrl b (== ctrl + click)
shift shift (search)
alt shift ctrl j
ctrl e
ctrl shift a
alt j
"""

@pytest.mark.parametrize('event,expected', [
    ('P....', '12345'),
    ('..........', '0000000000'),
    ('P.P..', '12222'),
    ('P......P......', '12345554321000'),
    ('..P...O...', '0012343210')
])
@pytest.mark.parametrize('function', [controller])
def test_killer_garage_door(event, expected, function):
    result = function(event)
    assert result == expected
