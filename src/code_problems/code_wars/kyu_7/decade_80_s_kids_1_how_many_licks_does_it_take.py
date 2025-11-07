def total_licks(env: dict):
    licks = 252
    high = -1
    for k, v in env.items():
        licks += v
        high = max(high, v)
    if high > 0:
        for k, v in env.items():
            if v == high:
                return (
                    f'It took {licks} licks to get '
                    f'to the tootsie roll center of '
                    f'a tootsie pop. The toughest challenge was {k}.'
                )
    return (
        f'It took {licks} licks to get to the '
        f'tootsie roll center of a tootsie pop.'
    )
