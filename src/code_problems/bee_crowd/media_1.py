# https://judge.beecrowd.com/pt/problems/view/1005


def media(nota_a, nota_b):
    media = nota_a * 3.5 + nota_b * 7.5
    return media / (3.5 + 7.5)


print(f'{media(5.0, 7.1):.5f}')


def is_odd(param):
    return param % 2 == 0


for col in range(10):
    col_is_odd = is_odd(col)
    for line in range(10):
        line_is_odd = is_odd(line)
        if (col_is_odd and line_is_odd) or (
            not col_is_odd and not line_is_odd
        ):
            print('X', end=' ')
        else:
            print('-', end=' ')
    print()
