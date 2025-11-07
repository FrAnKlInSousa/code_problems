def xbonacci(signature: list, n: int):
    size = len(signature)
    if n <= size:
        return signature[:n]

    for _ in range(size, n):
        signature.append(sum(signature[-size:]))
    return signature
