vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

def change_to_exclamation_mark(text: str) -> str:
    final_text = []
    for char in text:
        if char in vowels:
            final_text.append('!')
        else:
            final_text.append(char)

    return ''.join(final_text)

def change_to_exclamation_mark_regex(text: str) -> str:
    return text.translate(str.maketrans('aeiouAEIOU', '!'*10))
