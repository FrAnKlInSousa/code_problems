class Harshad:
    def is_valid(self, number: int):
        digits = list(str(number))
        digit_sum = sum(int(num) for num in digits)
        return number % digit_sum == 0

    def get_next(self):
        ...

    def get_serie(self):
        ...