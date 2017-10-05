def pyramid(n):
    pyramidString = ''
    for x in reversed(range(0, n)):
        pyramidString += (' ' * x) + '*' + (' *' * (n - 1 - x) + '\n')
    return pyramidString 

print(pyramid(10))
