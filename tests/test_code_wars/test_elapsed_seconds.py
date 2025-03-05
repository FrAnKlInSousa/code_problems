from datetime import datetime

import pytest

from src.code_problems.code_wars.kyu_7.elapsed_seconds import elapsed_seconds

start_date = datetime(2013, 1, 1, 0, 0, 1)
end_date = datetime(2013, 1, 1, 0, 0, 2)
end_date_2 = datetime(2013, 1, 1, 0, 0, 20)
end_date_3 = datetime(2013, 1, 1, 0, 1, 20)


@pytest.mark.parametrize(
    'start,end,expected',
    [
        (start_date, end_date, 1),
        (end_date, end_date_2, 18),
        (start_date, end_date_2, 19),
        (start_date, end_date_3, 79),
        (end_date, end_date_3, 78),
    ],
)
@pytest.mark.parametrize('function', [elapsed_seconds])
def test_elapsed_seconds(start, end, expected, function):
    result = function(start, end)
    assert result == expected
