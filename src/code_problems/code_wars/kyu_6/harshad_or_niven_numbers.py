class Harshad:
    @staticmethod
    def is_valid(number: int):
        digits = list(str(number))
        digit_sum = sum(int(num) for num in digits)
        if digit_sum == 0:
            return True
        return number % digit_sum == 0

    @staticmethod
    def get_next(number: int):
        number += 1
        while True:
            if Harshad().is_valid(number):
                return number
            number += 1

    @staticmethod
    def get_serie(): ...
