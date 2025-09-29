import pytest

from src.code_problems.code_wars.kyu_7.naughty_number import (
    naughty_number,
    naughty_number_clever,
)


@pytest.mark.parametrize(
    'arr,expected',
    [
        ([[[[]]], [[]], [], [], [[2]]], 4),
        ([[1]], 0),
        ([[], [8], [], []], 1),
        ([[[[[[[[[42]]]]]]]]], 0),
        ([[], [], [], [], [], [], [], [], [], [], [], [77]], 11),
        (
            [
                [[]],
                [[[[[]]]]],
                [],
                [[[[[[[[[]]]]]]]]],
                [[[]]],
                [[[[31]]]],
                [[]],
                [],
            ],
            5,
        ),
        ([[1], [[[[]]]], [[]], [[[[[[[[[]]]]]]]]], []], 0),
    ],
)
@pytest.mark.parametrize(
    'function', [naughty_number, naughty_number_clever]
)
def test_naughty_number(arr, expected, function):
    result = function(arr)
    assert result == expected
