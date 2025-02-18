def find_integral(coefficient, exponent):
    exponent += 1
    coefficient = int(int(coefficient) / int(exponent))
    return f'{coefficient}x^{exponent}'
