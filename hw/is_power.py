def is_power(n,b):
    if n == 1:
        return True
    if n == b:
        return True
    elif n < 1:
        return False
    return is_power(n / b, b)

