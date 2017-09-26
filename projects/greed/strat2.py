import math

dieMean = 2.5
dieVariance = 2.9166666666667

def findSafe(risk):
    maxSafe = 1
    while currentProb < risk:
        maxSafe += 1
    return maxSafe

def create(verbose):
    def strategy(myScore, theirScore, isLast):
        return findSafe(0.15)    
    return strategy
