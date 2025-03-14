import re


def remove_extra_spaces(phrase):
    return re.sub(r'\s+', ' ', phrase).strip()
