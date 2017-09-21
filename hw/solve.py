import math

def isInt(i):
    remainder = i % 1
    if remainder > 0.0:
        return False
    return True

# def sqrt(n):
#     x = n
#     y = (x + 1) // 2
#     while y < x:
#         x = y
#         y = (x + n // x) // 2
#     return x

def solve(a,b,c):
    discriminator = b**2 - 4*a*c
    if discriminator < 0:
        return False
    x = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    y = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    if isInt(x) and isInt(y):
        if x > y:
            return int(x)
        return int(y)
    elif isInt(x) and isInt(y) == False:
        return int(x)
    elif isInt(y) and isInt(x) == False:
        return int(y)
    return False

# print(solve(1,-1,-30))
