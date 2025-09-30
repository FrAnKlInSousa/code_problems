
def hex_color(codes: str):

    if codes in ['', '000 000 000']:
        return 'black'
    r, g, b = codes.split()

    if r == g and b < r:
        return 'yellow'
    elif b < g > r:
        return 'green'
    elif g < b > r:
        return 'blue'
    elif b < r > g:
        return 'red'
    elif g == b and r < g:
        return 'cyan'
    elif r == b and g < r:
        return 'magenta'
    return 'white'
