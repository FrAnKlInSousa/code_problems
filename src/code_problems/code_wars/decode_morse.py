import re

from preload import MORSE_CODE

# https://www.codewars.com/kata/54b724efac3d5402db00065e
WORD_SEP = ' ' * 3


def decode_morse(morse_message: str) -> str:
    def remove_duplicated_spaces(word: str):
        """
        remove duplicated blank spaces from the
        start and end of the str
        '   In this   example  the result will  be  ':
        'In this example the result will be'
        """

        return re.sub(' {2,}', ' ', word).strip()

    splited_words = morse_message.split(WORD_SEP)
    splited_words = [remove_duplicated_spaces(word) for word in splited_words]
    phrase = []
    for word in splited_words:
        split_letters = word.split(' ')
        actual_word = []
        for letter in split_letters:
            if letter:
                actual_word.append(MORSE_CODE[letter])

        translated_word = ''.join(actual_word)
        if translated_word:
            phrase.append(translated_word)
    temp_phrase = ' '.join(phrase)
    final_phrase = remove_duplicated_spaces(temp_phrase)

    return final_phrase


def decode_morse_clever(morse_message: str):
    morse_data = morse_message.strip().replace('   ', ' * ')
    translated_msg = ''

    for data in morse_data.split():
        if data != '*':
            translated_msg += MORSE_CODE[data]
        else:
            translated_msg += ' '
    return translated_msg
