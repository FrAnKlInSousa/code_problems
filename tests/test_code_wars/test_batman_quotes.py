import pytest

from src.code_problems.code_wars.kyu_7.batman_quotes import BatmanQuotes, BatmanQuotesClever


@pytest.mark.parametrize('quotes,hero,expected', [
    (["WHERE IS SHE?!", "Holy haberdashery, Batman!", "Let's put a smile on that faaaceee!"], 'Rob1n', 'Robin: Holy haberdashery, Batman!'),
])
@pytest.mark.parametrize('function', [BatmanQuotes.get_quote, BatmanQuotesClever.get_quote])
def test_batman_quotes(quotes, hero, expected, function):
    result = function(quotes, hero)
    assert result == expected
