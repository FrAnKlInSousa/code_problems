import pytest

from src.code_problems.code_wars.kyu_7.colored_hexes import hex_color


@pytest.mark.parametrize('color,expected', [
    ('', 'black'),
('000 000 000', 'black'),
('121 245 255', 'blue'),
('027 100 100', 'cyan'),
('021 021 021', 'white'),
('255 000 000', 'red'),
('000 147 000', 'green'),
('212 103 212', 'magenta'),
('101 101 092', 'yellow'),
])
@pytest.mark.parametrize('function', [hex_color])
def test_dropzone(color, expected, function):
    result = function(color)
    assert result == expected
