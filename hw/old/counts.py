def counts(n, xs):
    occurances = []
    for targetN in range(0, n):
        target = targetN 
        thisOccurances = 0
        for val in xs:
            if val == target:
                thisOccurances += 1
        occurances.append(thisOccurances)
    return occurances
            
