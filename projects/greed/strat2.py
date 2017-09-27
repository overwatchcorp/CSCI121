dieMean = 2.5
dieVariance = 2.9166666666667

'''
strategy 2
----------
if my score is less than 70, divide the remaining score (100 - myScore) by the mean of a die roll and multiply by a multiplier (chosen mildly randomly--I just fiddled around with the numbers for a while
if my score is more than 70, do the same thing but use a slightly lower multiplyer
if my score is less than my opponent's score AND my score is greater than 95, roll 1 die
'''
def strategy(myScore, theirScore, isLast):
    remainingScore = 100 - myScore
    if theirScore > myScore and myScore > 95:
        return 1
    if myScore < 70:
        return int(remainingScore / dieMean * 0.86)
    return int(remainingScore / dieMean * 0.80) 
