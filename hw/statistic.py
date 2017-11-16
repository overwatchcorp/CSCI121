def selectionsort (aList):
    aLen = len(aList)
    # go from pos 0 to end of array
    for x in range(aLen):
        minVal = aList[x]
        minIndex = x
        # iterates over array again, since we have 2 for loops, time is Θ(n^2)
        for y in range(x, aLen):
            if aList[y] < minVal:
                minVal = aList[y]
                minIndex = y
        aList[x], aList[minIndex] = aList[minIndex], aList[x]

def statistic(i, aList):
    # selection sort runs in Θ(n^2) time
    selectionsort(aList)
    ith = []
    x = 0
    # single loop adds one n, so statistic runs in Θ(n^3) time
    while len(ith) <= i:
        ith.append(aList[x])
        x += 1
    return ith[-1]

