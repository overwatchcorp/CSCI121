def has_duplicates(xs):
    items = {}
    for x in xs:
        if x not in items:
            items[x] = True
        elif items[x] == True:
            return True
    return False

