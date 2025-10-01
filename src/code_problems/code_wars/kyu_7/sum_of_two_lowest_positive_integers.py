from heapq import nsmallest


def sum_two_smallest_numbers(numbers: list[int]) -> int:
    return sum(sorted(numbers)[:2])


def sum_two_smallest_numbers_faster(numbers):
    primeiro = float('inf')
    segundo = float('inf')

    for num in numbers:
        if num < primeiro:
            segundo = primeiro
            primeiro = num
        elif num < segundo:
            segundo = num

    return primeiro + segundo


def sum_two_smallest_numbers_alternative(numbers):
    return sum(nsmallest(2, numbers))
