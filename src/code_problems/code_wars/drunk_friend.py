"""
https://www.codewars.com/kata/558ffec0f0584f24250000a0/train/python
"""

from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from typing import Any


def drunk_friend(text: Any) -> str:
    if not isinstance(text, str):
        return 'Input is not a string'
    lower_letters = '_' + ascii_lowercase
    upper_letters = '_' + ascii_uppercase

    def translate(word):
        translated = []
        for letter in word:
            if letter in punctuation or letter in digits:
                translated.append(letter)
                continue
            if letter in lower_letters:
                translated.append(lower_letters[-lower_letters.index(letter)])
            else:
                translated.append(upper_letters[-upper_letters.index(letter)])
        return ''.join(translated)

    return ' '.join(
        translate(word) if word.isascii() else word for word in text.split(' ')
    )
