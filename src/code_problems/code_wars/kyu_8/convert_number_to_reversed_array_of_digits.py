def invert_number(number: int) -> list:
    number_str = list(str(number))
    return list(map(int, number_str[::-1]))
