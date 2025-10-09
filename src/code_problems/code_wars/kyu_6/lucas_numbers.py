def lucas_num(n: int) -> int:
    # solução é do @keeprocking (https://www.codewars.com/users/keeprocking)

    a = 2
    b = 1

    flip = n < 0 and n % 2 != 0

    for i in range(abs(n)):
        a, b = b, a + b

    return -a if flip else a
