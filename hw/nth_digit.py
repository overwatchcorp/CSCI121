def digit(x, n):
    tenToNth = 10 ** n
    nthDigit = x // tenToNth % 10
    return nthDigit
