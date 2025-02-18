# https://www.codewars.com/kata/51b62bf6a9c58071c600001b/python

MAX_REPETITION = 3


def roman_numeral_encoder(number: int) -> str:
    roman_table = {
        1: 'I',
        5: 'V',
        4: 'IV',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M',
    }
    divisors = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman = []
    while number > 0:
        for div in divisors:
            count = 0
            while div <= number and count <= MAX_REPETITION:
                number -= div
                count += 1
                roman.append(roman_table[div])
    return ''.join(roman)


def roman_numeral_encoder_gpt(number: int) -> str:
    roman_table = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I',
    }

    roman = []

    for value, symbol in roman_table.items():
        count, number = divmod(number, value)
        roman.append(symbol * count)

    return ''.join(roman)
