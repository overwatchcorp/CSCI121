def threeSum(ls, t):
    if len(ls) <= 2:
        return False
    for i, a in enumerate(ls):
        for y, b in enumerate(ls):
            for z, c in enumerate(ls):
                if i != z and i != y and y != z:
                    if a + b + c == t:
                        return True
    return False


