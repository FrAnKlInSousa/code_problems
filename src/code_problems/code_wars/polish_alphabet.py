def polish(word: str):
    alphabet = {
        'ą': 'a',
        'ć': 'c',
        'ę': 'e',
        'ł': 'l',
        'ń': 'n',
        'ó': 'o',
        'ś': 's',
        'ź': 'z',
        'ż': 'z',
    }

    list_word = list(word)
    for index, char in enumerate(list_word):
        if char in alphabet:
            list_word[index] = alphabet[char]
    final_word = ''.join(list_word)
    return final_word


def polish_alternative(word: str):
    alphabet = {
        'ą': 'a',
        'ć': 'c',
        'ę': 'e',
        'ł': 'l',
        'ń': 'n',
        'ó': 'o',
        'ś': 's',
        'ź': 'z',
        'ż': 'z',
    }
    translate_table = str.maketrans(alphabet)
    return word.translate(translate_table)
