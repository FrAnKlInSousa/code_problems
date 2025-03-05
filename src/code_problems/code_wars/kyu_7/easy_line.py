from math import comb, factorial


def easy_line(line_number: int) -> int:
    total = 0

    line_number_fact = factorial(line_number)

    for element in range(0, line_number + 1):
        total += (
            line_number_fact
            // (factorial(element) * (factorial(line_number - element)))
        ) ** 2
    return int(total)


def easy_line_clever(number_line):
    return sum(
        (comb(number_line, element)) ** 2
        for element in range(0, number_line + 1)
    )
