celestial_order = {
    'Asteroid': 0,
    'Pluto': 1,
    'Mercury': 2,
    'Mars': 3,
    'Venus': 4,
    'Earth': 5,
    'Neptune': 6,
    'Uranus': 7,
    'Saturn': 8,
    'Jupiter': 9,
}


def solar_system_jumbled_planets(astronomical_objects: list) -> list:
    prev = None
    order = []
    for index, obj in enumerate(astronomical_objects):
        if index == 0:
            prev = obj
            continue
        if celestial_order[obj] > celestial_order[prev]:
            order.append('>')
        elif celestial_order[obj] < celestial_order[prev]:
            order.append('<')
        else:
            order.append('=')
        prev = obj
    return order
