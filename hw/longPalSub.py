def isPal (n):
    nReversed = n[::-1]
    if n == nReversed:
        return True
    else:
        return False

def longPalSub (n):
    longest = ''
    # cache previously checked palindromes
    # prevents us from having to do many of the same array slices on long passages
    cache = {}
    for x in range(len(n)):
        for y in range(x, len(n) + 1):
            # if x and y are equal, we will have an empty slice; don't run if x and y are equal
            if x != y:
                testPal = n[x:y]
                if testPal not in cache:
                    testIsPal = isPal(testPal)
                    cache[testPal] = testIsPal
                    if testIsPal:
                        if len(testPal) > len(longest):
                            longest = testPal
    return longest

# import timeit

# print(timeit.timeit('longPalSub("cbcbaabacaor")', setup='from __main__ import longPalSub', number=100000))
