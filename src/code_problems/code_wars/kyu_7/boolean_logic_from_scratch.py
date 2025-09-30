def func_or(a, b):
    if a:
        return True
    elif b:
        return True
    return False


def func_or_clever(a, b):
    return bool(bool(a) + bool(b))


def func_xor(a, b):
    if a and not b:
        return True
    elif b and not a:
        return True
    return False

def func_xor_clever(a, b):
    if bool(a) is bool(b):
        return False
    return True

def func_xor_clever_2(a, b):
    return bool(a) is not bool(b)