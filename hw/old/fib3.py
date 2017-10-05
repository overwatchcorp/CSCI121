def fib3(n):
    fibVals = []
    for x in range(0, n):
        if x < 2:
            fibVals.append(1)
        elif x == 2:
            fibVals.append(2)
        else:
            index = len(fibVals)
            nextVal = fibVals[index - 3:index]
            fibVals.append(sum(nextVal))
    return(fibVals[n - 1])
print(fib3(8))
