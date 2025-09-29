def time_convert(num) -> str:
    if num <= 0:
        return '00:00'
    minutes = num % 60
    hours = (num - minutes) // 60
    return f'{hours}'.zfill(2) + ':' + f'{minutes}'.zfill(2)

def time_convert_clever(num) -> str:
    if num <= 0:
        return '00:00'

    hours, minutes = divmod(num, 60)
    return f'{hours:02}:{minutes:02}'
