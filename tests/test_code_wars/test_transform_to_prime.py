import pytest

from src.code_problems.code_wars.transform_to_prime import transform_to_prime


@pytest.mark.parametrize('numbers,expected', [
    ([3, 1, 2], 1),
    ([2, 12, 8, 4, 6], 5),
    ([50, 39, 49, 6, 17, 28], 2)
])
def test_transform_to_prime(numbers, expected):
    result = transform_to_prime(numbers)
    assert result == expected