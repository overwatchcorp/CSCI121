def poly2max(xmin, xmax, ymin, ymax):
    largestZ = None
    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            equationVal = -x**4 + 3*x**2 - y**4 + 5*y**2
            if largestZ== None:
                largestZ = equationVal
            if equationVal > largestZ:
                largestZ = equationVal
    return largestZ

# print(poly2max(0, 5, 7, 7))
