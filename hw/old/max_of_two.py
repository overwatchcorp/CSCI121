def max_of_two(f1, f2, n):
    f1val = f1(n)
    f2val = f2(n)
    if f1val > f2val:
        return f1val
    return f2val

