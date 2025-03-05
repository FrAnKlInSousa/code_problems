import pytest

from src.code_problems.code_wars.kyu_7.the_solar_system_jumbled_planets import (
    solar_system_jumbled_planets,
)


@pytest.mark.parametrize(
    'astronomical_objects,expected',
    [
        (
            [
                'Mars',
                'Asteroid',
                'Venus',
                'Jupiter',
                'Asteroid',
                'Earth',
                'Pluto',
            ],
            ['<', '>', '>', '<', '>', '<'],
        ),
        (['Venus', 'Jupiter', 'Mercury'], ['>', '<']),
        ([], []),
        (['Earth'], []),
        (
            ['Saturn', 'Venus', 'Mars', 'Pluto', 'Asteroid'],
            ['<', '<', '<', '<'],
        ),
        (['Asteroid', 'Neptune', 'Jupiter', 'Saturn'], ['>', '>', '<']),
        (
            [
                'Venus',
                'Mars',
                'Neptune',
                'Uranus',
                'Earth',
                'Jupiter',
                'Mercury',
            ],
            ['<', '>', '>', '<', '>', '<'],
        ),
        (
            [
                'Pluto',
                'Neptune',
                'Mercury',
                'Venus',
                'Uranus',
                'Mars',
                'Earth',
                'Jupiter',
                'Asteroid',
                'Saturn',
                'Asteroid',
                'Asteroid',
                'Asteroid',
                'Asteroid',
            ],
            ['>', '<', '>', '>', '<', '>', '>', '<', '>', '<', '=', '=', '='],
        ),
    ],
)
def test_solar_system_jumbled_planets(astronomical_objects, expected):
    result = solar_system_jumbled_planets(astronomical_objects)
    assert result == expected
