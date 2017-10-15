def collatz(n):
    steps = 1 
    currentInt = n
    while currentInt != 1:
        # print(steps, int(currentInt))
        modInt = currentInt % 2
        if modInt == 1:
            currentInt = currentInt * 3 + 1
        else:
            currentInt = currentInt / 2
        steps += 1
        if steps == n:
            return int(currentInt)
    return steps

# print(collatz(10))
# 7 should return 3
