from typing import List


def calculate_box_sizes(width, height, depth) -> List[int]:
    width_height_area = width * height
    area = 2 * (width_height_area + depth * height + depth * width)
    volume = width_height_area * depth
    return [area, volume]
