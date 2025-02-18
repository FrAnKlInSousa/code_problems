import pytest

from src.code_problems.code_wars.best_travel import (
    best_travel,
    best_travel_variant,
)

xs_01 = [
    100,
    76,
    56,
    44,
    89,
    73,
    68,
    56,
    64,
    123,
    2333,
    144,
    50,
    132,
    123,
    34,
    89,
]


@pytest.mark.parametrize(
    'max_distance,num_towns,distances,expected', [(230, 4, xs_01, 230)]
)
@pytest.mark.parametrize('function', [best_travel, best_travel_variant])
def test_best_travel_01(
    max_distance, num_towns, distances, expected, function
):
    result = function(max_distance, num_towns, distances)
    assert result == expected


ts_02 = [50, 55, 56, 57, 58]


@pytest.mark.parametrize(
    'max_distance,num_towns,distances,expected', [(163, 3, ts_02, 163)]
)
@pytest.mark.parametrize('function', [best_travel, best_travel_variant])
def test_best_travel_02(
    max_distance, num_towns, distances, expected, function
):
    result = function(max_distance, num_towns, distances)
    assert result == expected


ts_03 = [50]


@pytest.mark.parametrize(
    'max_distance,num_towns,distances,expected', [(163, 3, ts_03, None)]
)
@pytest.mark.parametrize('function', [best_travel, best_travel_variant])
def test_best_travel_03(
    max_distance, num_towns, distances, expected, function
):
    result = function(max_distance, num_towns, distances)
    assert result == expected


ts_04 = [91, 74, 73, 85, 73, 81, 87]


@pytest.mark.parametrize(
    'max_distance,num_towns,distances,expected',
    [
        (230, 3, ts_04, 228),
        (331, 2, ts_04, 178),
        (331, 4, ts_04, 331),
        (331, 5, ts_04, None),
        (331, 1, ts_04, 91),
        (700, 6, ts_04, 491),
    ],
)
@pytest.mark.parametrize('function', [best_travel, best_travel_variant])
def test_best_travel_04(
    max_distance, num_towns, distances, expected, function
):
    result = function(max_distance, num_towns, distances)
    assert result == expected


xs_05 = [
    100,
    76,
    56,
    44,
    89,
    73,
    68,
    56,
    64,
    123,
    2333,
    144,
    50,
    132,
    123,
    34,
    89,
]


@pytest.mark.parametrize(
    'max_distance,num_towns,distances,expected',
    [
        (230, 4, xs_05, 230),
        (430, 5, xs_05, 430),
        (430, 8, xs_05, None),
        (880, 8, xs_05, 876),
        (2430, 15, xs_05, 1287),
        (100, 2, xs_05, 100),
        (276, 3, xs_05, 276),
        (3760, 17, xs_05, 3654),
        (3760, 40, xs_05, None),
        (50, 1, xs_05, 50),
        (1000, 18, xs_05, None),
    ],
)
@pytest.mark.parametrize('function', [best_travel, best_travel_variant])
def test_best_travel_05(
    max_distance, num_towns, distances, expected, function
):
    result = function(max_distance, num_towns, distances)
    assert result == expected


xs_06 = [100, 64, 123, 2333, 144, 50, 132, 123, 34, 89]


@pytest.mark.parametrize(
    'max_distance,num_towns,distances,expected',
    [
        (230, 4, xs_06, None),
        (230, 2, xs_06, 223),
        (2333, 1, xs_06, 2333),
        (2333, 8, xs_06, 825),
    ],
)
@pytest.mark.parametrize('function', [best_travel, best_travel_variant])
def test_best_travel_06(
    max_distance, num_towns, distances, expected, function
):
    result = function(max_distance, num_towns, distances)
    assert result == expected


xs_07 = [1000, 640, 1230, 2333, 1440, 500, 1320, 1230, 340, 890, 732, 1346]


@pytest.mark.parametrize(
    'max_distance,num_towns,distances,expected',
    [
        (2300, 4, xs_07, 2212),
        (2300, 5, xs_07, None),
        (2332, 3, xs_07, 2326),
        (23331, 8, xs_07, 10789),
        (331, 2, xs_07, None),
    ],
)
@pytest.mark.parametrize('function', [best_travel, best_travel_variant])
def test_best_travel_06(
    max_distance, num_towns, distances, expected, function
):
    result = function(max_distance, num_towns, distances)
    assert result == expected
