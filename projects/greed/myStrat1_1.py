import numpy 
from scipy.stats import norm

dieMean = 2.5
dieVariance = 2.9166666666667

# risk is the odds the script will overshoot 100 (lose)
def create(risk, verbose):
    def play(myScore, theirScore, isLast):
        remainingScore = 100 - myScore
        print('remaining: ', remainingScore) if verbose == True else None
        # cap is the hgihest number of die that one could roll, given the mean of the die
        cap = int(remainingScore / dieMean)
        # we init maxSafe with the highest number of die, but we will deincrement until a safe number is found
        maxSafe = cap
        searching = True
        currentRisk = risk
        # if theirScore > 0 and myScore / theirScore < 1.5:
        #     currentRisk += myScore / theirScore * 0.15 
        # if theirScore > 80:
        #      currentRisk += 
        if theirScore > 95:
             currentRisk += risk * 10
        while searching:
            check = maxSafe
            mean = dieMean * check
            deviation = numpy.sqrt(dieVariance * check)
            zScore = (remainingScore - mean) / deviation
            if zScore < 1.036599999999996:
                overshootOdds = 1
            else:
                overshootOdds = norm.sf(zScore)
            print('checked: ', check, ' overshoot prob: ', overshootOdds, zScore) if verbose == True else None
            if overshootOdds < currentRisk:
                maxSafe = check
                searching = False
            else:
                maxSafe -= 1
            if maxSafe <= 0:
                break
        # if myScore < theirScore and remainingScore <= 5:
        #     return 3
        return maxSafe
    return play
