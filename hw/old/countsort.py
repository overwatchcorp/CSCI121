def countsort(aList, m):
    # for loops run in n time, so asymptotic complexity is n
    counts = [0] * m
    for i in aList:
        counts[i] += 1
    sortedList = []
    for x, p in enumerate(counts):
        sortedList += ([x] * p)
    print(sortedList)
    aList = sortedList

toSort = [1, 2, 0, 0, 1, 3, 2, 1, 0, 1, 3, 3, 3, 1, 0, 1, 0]
countsort(toSort, 4)
print(toSort)
