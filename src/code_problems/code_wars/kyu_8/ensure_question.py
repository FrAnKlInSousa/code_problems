def ensure_question(phrase: str) -> str:
    if phrase:
        return f'{phrase}?' if phrase[-1] != '?' else phrase
    return f'{phrase}?'
