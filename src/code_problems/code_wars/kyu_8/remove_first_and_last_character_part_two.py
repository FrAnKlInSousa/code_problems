def array(string: str) -> str | None:
    string = string.split(',')
    def _remove_first_and_last(string_list: list) -> list:
        return string_list[1:len(string)-1]
    if len(string) < 3:
        return None
    string = _remove_first_and_last(string)
    return ' '.join(string)
