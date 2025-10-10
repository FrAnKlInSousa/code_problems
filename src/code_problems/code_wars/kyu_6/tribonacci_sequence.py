def tribonacci(signature: list, n):
    match n:
        case 0:
            return []
        case 1:
            return signature[:1]
        case 2:
            return signature[:2]
        case _:
            size = len(signature)
            while n > size:
                signature.append(sum(signature[-3:]))
                size += 1
            return signature

def tribonacci_clever(signature: list, n):
    if n < 4:
        return signature[:n]
    size = len(signature)
    while size < n:
        signature.append(sum(signature[-3:]))
        size += 1
    return signature