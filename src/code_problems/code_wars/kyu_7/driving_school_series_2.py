BASE_COST = 30
EXTRA_COST_PER_HALF_HOUR = 10
FULL_HOUR = 60
HALF_HOUR = 30
GRACE_PERIOD = 5


def calculate_charge(lesson_duration: int) -> int:
    if lesson_duration <= FULL_HOUR:
        return BASE_COST

    extra_time = lesson_duration - FULL_HOUR

    if extra_time % HALF_HOUR > GRACE_PERIOD:
        extra_time += HALF_HOUR

    extra_cost = (extra_time // HALF_HOUR) * EXTRA_COST_PER_HALF_HOUR
    return BASE_COST + extra_cost
