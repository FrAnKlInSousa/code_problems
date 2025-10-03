def find_longest2(arr):
    highest = 0
    for num in arr:
        aux = len(str(num))
        if aux > len(str(highest)):
            highest = num
    return highest


for x in range(len([2,3,3,3,9])):
    print(find_longest2([x]))