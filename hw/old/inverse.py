def inverse(d):
    items = {}
    for i in d:
        if d[i] not in items:
            items[d[i]] = [i]
        else:
            items[d[i]].append(i)
    return items

