import numpy 
from scipy.stats import norm

dieMean = 2.5
dieVariance = 2.9166666666667

# risk is the odds the script will overshoot 100 (lose)
def create(risk, verbose):
    def play(myScore, theirScore, isLast):
        remainingScore = 100 - myScore
        print('remaining: ', remainingScore) if verbose == True else None
        maxSafe = 0
        searching = True
        while searching:
            check = maxSafe + 1
            thisMean = dieMean * check
            thisVariance = dieVariance * check
            thisDeviation = numpy.sqrt(thisVariance)
            zScore = (remainingScore - thisMean) / thisDeviation
            if zScore > 1.687:
                overshootOdds = 0.0000001
            else:
                overshootOdds = norm.sf(zScore)
            print('checked: ', check, ' overshoot prob: ', overshootOdds, zScore) if verbose == True else None
            if overshootOdds < risk:
                maxSafe = check
            else:
                searching = False
        return maxSafe
    return play
