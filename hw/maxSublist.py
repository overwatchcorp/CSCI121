def maxSublist (xs):
    lxs = len(xs)
    highest = 0
    highestStart = 0
    highestEnd = 0
    for x in range(lxs + 1):
        for y in range(x, lxs + 1):
            thisSum = sum(xs[x:y])
            if thisSum > highest:
              highest = thisSum
              highestStart = x
              highestEnd = y
    return xs[highestStart:highestEnd]

