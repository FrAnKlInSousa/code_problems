"""
https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python
"""

from string import punctuation


def simple_pig_latin(phrase: str) -> str:
    def move_first_letter_and_add_sufix(word: str) -> str:
        w = list(word)
        w.append(w[0])
        w.remove(w[0])
        return ''.join(w) + 'ay'

    words = phrase.split()
    final_phrase = []

    for word in words:
        if word not in punctuation:
            final_phrase.append(move_first_letter_and_add_sufix(word))
        else:
            final_phrase.append(word)
    return ' '.join(final_phrase).strip()


def simple_pig_latin_gpt(phrase: str) -> str:
    return ' '.join(
        word[1:] + word[0] + 'ay' if word.isalnum() else word
        for word in phrase.split()
    )
