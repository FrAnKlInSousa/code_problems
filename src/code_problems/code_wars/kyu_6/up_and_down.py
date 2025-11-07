def arrange(strng: str):
    result = strng.split()
    count = 0
    size = len(result)

    while size > (count + 1):
        if count % 2 == 0:
            if len(result[count]) > len(result[count + 1]):
                aux = result[count]
                result[count] = result[count + 1].lower()
                result[count + 1] = aux.upper()
            else:
                result[count] = result[count].lower()
                result[count + 1] = result[count + 1].upper()
        elif len(result[count]) < len(result[count + 1]):
            aux = result[count]
            result[count] = result[count + 1].upper()
            result[count + 1] = aux.lower()
        else:
            result[count] = result[count].upper()
            result[count + 1] = result[count + 1].lower()
        count += 1
    return ' '.join(result)
