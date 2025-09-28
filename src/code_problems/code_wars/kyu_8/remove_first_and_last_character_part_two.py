def array(string: str) -> str | None:
    string = string.split(',')
    min_len = 3

    def _remove_first_and_last(string_list: list) -> list:
        return string_list[1 : len(string) - 1]

    if len(string) < min_len:
        return None
    string = _remove_first_and_last(string)
    return ' '.join(string)
