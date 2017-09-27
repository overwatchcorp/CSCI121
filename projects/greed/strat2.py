dieMean = 2.5
dieVariance = 2.9166666666667

def create():
    def strategy(myScore, theirScore, isLast):
        remainingScore = 100 - myScore
        if theirScore > myScore and myScore > 95:
            return 1
        if myScore < 70:
            return int(remainingScore / dieMean * 0.86)
        return int(remainingScore / dieMean * 0.80) 
    return strategy
