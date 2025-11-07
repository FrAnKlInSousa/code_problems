from math import sqrt


def area(diagonal, side):
    """
    d: diagonal
    h: side
    d² = b² + h² -> d = √(b² + h²)
    area = b * h
    """
    if diagonal <= side:
        return 'Not a rectangle'
    base_powered = pow(diagonal, 2) - pow(side, 2)
    base = sqrt(base_powered)
    area_rec = base * side
    if not area_rec.is_integer():
        return round(area_rec, 2)
    return int(area_rec)
