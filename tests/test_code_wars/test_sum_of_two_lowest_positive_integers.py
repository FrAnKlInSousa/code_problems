

import pytest

from src.code_problems.code_wars.kyu_7.sum_of_two_lowest_positive_integers import sum_two_smallest_numbers, \
    sum_two_smallest_numbers_faster, sum_two_smallest_numbers_alternative


@pytest.mark.parametrize('numbers,expected', [
    ([10, 343445353, 3453445, 3453545353453], 3453455),
    ([5, 8, 12, 18, 22], 13),
    ([7, 15, 12, 18, 22], 19),
    ([25, 42, 12, 18, 22], 30),
])
@pytest.mark.parametrize('function', [sum_two_smallest_numbers, sum_two_smallest_numbers_faster, sum_two_smallest_numbers_alternative])
def test_sum_of_two_lowest_positive_integers(numbers, expected, function):
    result = function(numbers)
    assert result == expected
