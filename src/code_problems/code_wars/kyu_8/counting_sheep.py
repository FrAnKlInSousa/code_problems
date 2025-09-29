def count_sheeps(sheeps: list) -> int:
    if not sheeps:
        return 0
    return sheeps.count(True)
