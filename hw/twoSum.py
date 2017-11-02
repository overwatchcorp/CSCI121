import random 
import timeit

def twoSum(ls, t):
    if len(ls) <= 1:
        return False
    for i, n in enumerate(ls):
        for x, b in enumerate(ls):
            if i != x:
                if n + b == t:
                    return True
    return False

sampleInts = [791, 488, 799, 642, 16, 646, 792, 650, 950, 748, 505, 113, 256, 777, 242, 762, 94, 241, 422, 794, 349, 393, 206, 376, 264, 949, 35, 573, 996, 261, 982, 42, 689, 614, 615, 450, 148, 613, 65, 369, 274, 236, 233, 892, 234, 624, 164, 754, 633, 803, 570, 991, 146, 960, 889, 339, 832, 532, 100, 823, 165, 760, 699, 461, 653, 452, 119, 658, 329, 656, 547, 319, 755, 124, 135, 628, 900, 275, 379, 863, 21, 231, 831, 778, 915, 919, 580, 13, 943, 626, 205, 23, 585, 807, 616, 24, 971, 830, 467, 333]
sampleTarget = 256
print(twoSum(sampleInts, sampleTarget))
print(timeit.timeit('twoSum(sampleInts, sampleTarget)', setup="from __main__ import twoSum, sampleInts, sampleTarget", number=10000))
