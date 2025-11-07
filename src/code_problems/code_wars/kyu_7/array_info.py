def _array_len(array):
    return [len(array)]


def _int_count(array):
    count = len([item for item in array if type(item) is int])
    if count == 0:
        return [None]
    return [count]


def _float_count(array):
    count = len([item for item in array if type(item) is float])
    if count == 0:
        return [None]
    return [count]


def _str_count(array):
    def _remove_blank_spaces(string):
        return ''.join(string.split())

    count = len([
        item
        for item in array
        if type(item) is str and _remove_blank_spaces(item)
    ])
    if count == 0:
        return [None]
    return [count]


def _blank_spaces_count(array):
    blank_spaces = 0

    for item in array:
        if type(item) is str:
            blank_spaces += item.count(' ')
    if blank_spaces == 0:
        return [None]
    return [blank_spaces]


def array_info(array):
    if not array:
        return 'Nothing in the array!'

    result = []
    result.append(_array_len(array))
    result.append(_int_count(array))
    result.append(_float_count(array))
    result.append(_str_count(array))
    result.append(_blank_spaces_count(array))
    return result


def array_info_clever(array):
    if not array:
        return 'Nothing in the array!'
    return [
        [len(array)],
        [sum(isinstance(item, int) for item in array) or None],
        [sum(isinstance(item, float) for item in array) or None],
        [
            sum(isinstance(item, str) and not item.isspace() for item in array)
            or None
        ],
        [
            sum(isinstance(item, str) and item.isspace() for item in array)
            or None
        ],
    ]
