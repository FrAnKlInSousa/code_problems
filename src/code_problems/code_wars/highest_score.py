from string import ascii_lowercase

from preload import LETTER_VALUES

# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/


def highest_score(phrase: str) -> str:
    high_word = ''
    score = 0

    words = phrase.split()
    for word in words:
        partial_score = 0
        for char in word:
            partial_score += LETTER_VALUES[char]
        if partial_score > score:
            score = partial_score
            high_word = word

    return high_word


def highest_score_clever(phrase: str) -> str:
    alphabet = '_' + ''.join([letter for letter in ascii_lowercase])
    highest_word = ''
    score = 0
    words = phrase.split()

    for word in words:
        partial_score = 0
        for char in word:
            # o index() percorre a lista a cada iteração,
            # o que torna menos eficiente
            partial_score += alphabet.index(char)
        if partial_score > score:
            score = partial_score
            highest_word = word

    return highest_word


def highest_score_gpt(phrase: str) -> str:
    letter_values = {
        char: idx for idx, char in enumerate(ascii_lowercase, start=1)
    }

    def word_score(word: str) -> int:
        return sum(letter_values[char] for char in word)

    return max(phrase.split(), key=word_score)
