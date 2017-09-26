def max_of_funcs(f1, f2):
    def find_max(x):
        f1val = f1(x)
        f2val = f2(x)
        if f1val > f2val:
            return f1val
        return f2val
    return find_max
