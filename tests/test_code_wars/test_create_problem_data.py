import pytest

from src.utils.create_problem_data import format_name


@pytest.mark.parametrize('word,expected', [
    ('The Solar System - Jumbled Planets', 'the_solar_system_jumbled_planets'),
    ('Driving School Series #2', 'driving_school_series_2')
])
def test_format_name(word, expected):
    result = format_name(word)
    assert result == expected