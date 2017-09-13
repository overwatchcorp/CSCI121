import random
import numpy
import scipy.stats as st
import time 
capNonInclusive = 100
confidenceLevel = 0.05

def roll():
    dieValue = random.randrange(1, 6)
    return dieValue

def rollMany(n):
    total = 0
    for i in range(0, n):
        value = roll()
        total += value
    return total

def computeAvgOfN(nDie, nRounds):
    roundValues = []
    for i in range(0, nRounds):
        roundValue = rollMany(nDie)
        roundValues.append(roundValue)
    total = 0
    for i in range(len(roundValues)):
        total += roundValues[i]
    results = {}
    results['mean'] = numpy.mean(roundValues)
    results['std'] = numpy.std(roundValues)
    if results['std'] == 0:
        results['std'] = 0.000000001
    zscore = (capNonInclusive - results['mean']) / results['std']
    results['percentile'] = st.norm.sf(zscore) 
    return results

startedAt = time.time()
highestN = 0
for x in range(0, 33):
    set = computeAvgOfN(x, 300)
    if set['percentile'] > confidenceLevel:
        # print(x, 'not safe', set['mean'], set['std'])
        break
    # print(x, 'safe', set['mean'], set['std'])
    highestN = x
print('selected: ', highestN)
rollValue = rollMany(highestN)
print('roll value: ', rollValue)
if rollValue > 99:
    print('LOSS :((((((')
else:
    print('ok! continue!')
endedAt = time.time()
