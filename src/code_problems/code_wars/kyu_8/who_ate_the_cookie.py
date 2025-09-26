def cookie(data):
    message = 'Who ate the last cookie? It was'

    if type(data) == str:
        return f'{message} Zach!'
    elif type(data) in [int, float]:
        return f'{message} Monica!'
    return f'{message} the dog!'

