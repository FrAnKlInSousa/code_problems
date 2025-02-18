def who_is_paying(neighbor: str):
    memorization_capacity = 2
    if len(neighbor) <= memorization_capacity:
        return [neighbor]
    return [neighbor, neighbor[:memorization_capacity:]]
