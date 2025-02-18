# https://judge.beecrowd.com/pt/problems/view/1239

def bloggo() -> None:
    phrase = input()
    closed_star = True
    closed_under = True
    final_phrase = []
    for char in phrase:
        if char == '*':
            if closed_star:
                closed_star = False
                final_phrase.append('<b>')
            else:
                closed_star = True
                final_phrase.append('</b>')
        if char == '_':
            if closed_under:
                closed_under = False
                final_phrase.append('<i>')
            else:
                closed_under = True
                final_phrase.append('</i>')
        if char not in ['*', '_']:
            final_phrase.append(char)
    print(''.join(final_phrase))

while True:
    try:
        bloggo()
    except EOFError:
        break