"""
https://www.codewars.com/kata/558ffec0f0584f24250000a0/train/python
"""

from string import ascii_lowercase, ascii_uppercase
from typing import Any


# todo fix me
def drunk_friend(text: Any) -> str:
    if not isinstance(text, str):
        return 'Input is not a string'
    lower_letters = '_' + ascii_lowercase
    upper_letters = '_' + ascii_uppercase

    # to fix
    def translate(word):
        translated = []
        for letter in word:
            if letter in lower_letters:
                translated.append(lower_letters[-lower_letters.index(letter)])
            else:
                translated.append(upper_letters[-upper_letters.index(letter)])
        return ''.join(translated)

    return ' '.join(
        translate(word) if word.isalpha() else word for word in text.split()
    )
