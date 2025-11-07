def find_longest(arr):
    highest = 0
    for num in arr:
        aux = len(str(num))
        if aux > len(str(highest)):
            highest = num
    return highest
