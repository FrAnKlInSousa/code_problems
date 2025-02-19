import pytest

from src.code_problems.code_wars.kyu_8.surface_area_and_volume_of_a_box import calculate_box_sizes


@pytest.mark.parametrize('width,height,depth,expected', [
    (4, 2, 6, [88,48]),
    (1, 1, 1, [6,1]),
    (1, 2, 1, [10,2]),
    (1, 2, 2, [16,4]),
    (10, 10, 10, [600,1000])
])
def test_calculate_box_sizes(width, height, depth, expected):
    result = calculate_box_sizes(width, height, depth)
    assert result == expected