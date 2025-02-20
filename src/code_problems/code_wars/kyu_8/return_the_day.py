days = {
    1: 'Sunday',
    2: 'Monday',
    3: 'Tuesday',
    4: 'Wednesday',
    5: 'Thursday',
    6: 'Friday',
    7: 'Saturday',
}
ERROR = 'Wrong, please enter a number between 1 and 7'


def what_day(number):
    if number in days:
        return days[number]
    return 'Wrong, please enter a number between 1 and 7'


def what_day_alternative(number):
    return days.get(number, ERROR)
