import random 
import numpy
import scipy.stats as st

rollMean = 3.5
rollVar = 105 / 36

def roll():
    rollVal = random.randrange(1, 6)
    return rollVal

def rollMany(n):
        total = 0
        for i in range(0, n):
            value = roll()
            total += value
        return total

def playRound(remainingScore):
    print('remaining score: ', remainingScore)
    safestN = 0
    valueSelected = False
    currentN = 1 
    while valueSelected == False:
        currentMean = rollMean * currentN
        currentVar = rollVar * currentN
        currentStd = numpy.sqrt(currentVar)
        maxValNonInclusive = remainingScore + 1
        currentZ = ( maxValNonInclusive - currentMean ) / currentStd
        percentOvershoot = st.norm.cdf(currentZ)
        print(currentN, currentMean, currentStd, currentZ, percentOvershoot)
        if numpy.absolute(percentOvershoot) < 0.95:
            valueSelected = True
        else:
            safestN = currentN
            currentN += 1
    print('safest number ', safestN)


playRound(100)
# playRound(99)
# playRound(50)
# playRound(7)
# playRound(6)
# playRound(3)
