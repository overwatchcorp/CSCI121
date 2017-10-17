def remainder(n,d):
    if n < 0:
        multi = -1
    else:
        multi = 1
    if 0<=n<d:
        return n
    else:
        return remainder(n - (d * multi), d)
