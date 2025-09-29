def remove_bmw(string: str) -> str:
    try:
        chars = ['B', 'M', 'W', 'b', 'm', 'w']
        for char in chars:
            string = string.replace(char, '')
        return string
    except Exception:
        raise TypeError('This program only works for text.')


def remove_bmw_clever(string: str) -> str:
    try:
        return string.translate(str.maketrans('', '', 'bmwBMW'))
    except Exception:
        raise TypeError('This program only works for text.')
