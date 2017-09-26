def isInt(n):
    remainder = n % 1
    if remainder > 0.0:
        return False
    return True

def sqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def solve(a,b,c):
    if (b**2 - 4*a*c) < 0:
        return False
    x = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
    y = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
    if isInt(x) and isInt(y):
        if y > x:
            return int(y // 1) 
        return int(x // 1)
    elif isInt(x) and isInt(y) == False:
        return int(x // 1)
    elif isInt(y) and isInt(x) == False:
        return int(y // 1)
    return False

# print(solve(1,2,1))
