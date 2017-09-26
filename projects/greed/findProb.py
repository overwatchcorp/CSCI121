from scipy.stats import norm
zscore = 1
cProb = norm.sf(zscore)
while cProb > 0.15:
    cProb = norm.sf(zscore)
    zscore += 0.0001
print(zscore, cProb)
