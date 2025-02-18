from itertools import combinations
from typing import List


def best_travel(maximum_distance: int, num_towns: int, distances: List[int]):
    distances_group = combinations(distances, num_towns)
    better_distance = [
        sum(distances)
        for distances in distances_group
        if sum(distances) <= maximum_distance
    ]
    better_distance.sort(reverse=True)
    if better_distance:
        return better_distance[0]


def best_travel_variant(
    maximum_distance: int, num_towns: int, distances: List[int]
):
    group_sum = combinations(distances, num_towns)
    return max(
        {sum(group) for group in group_sum if sum(group) <= maximum_distance},
        default=None,
    )
