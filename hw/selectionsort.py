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
                
