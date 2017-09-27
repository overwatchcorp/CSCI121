dieMean = 2.5
dieVariance = 2.9166666666667

def create(highThresh, highProb, normProb):
    def strategy(myScore, theirScore, isLast):
        remainingScore = 100 - myScore
        if theirScore > myScore and myScore > 95:
            return 1
        if myScore < highThresh:
            return int(remainingScore / dieMean * highProb)
        return int(remainingScore / dieMean * normProb) 
    return strategy
