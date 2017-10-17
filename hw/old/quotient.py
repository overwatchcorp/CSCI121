def quotient(n, d):
#    print(n,d)
    quotientSum = 0
    if n == d:
        quotientSum += 1
        return quotientSum
    if n > 0:
        if n > d:
            if (n - d) < d:
                return quotientSum + 1
            else:
                quotientSum += quotient(n - d, d) + 1
                return quotientSum
        else:
            if (n + d) > d and quotientSum == 0:
                return quotientSum
            elif (n + d) > d:
                return quotientSum - 1
            else:
                quotientSum += quotient(n + d, d) - 1
                return quotientSum
    elif n < d:
        if (n + d) > d:
            return quotientSum - 1
        else:
            quotientSum += quotient(n + d, d) - 1
            return quotientSum
   
# print(quotient(9, 10))
# print(quotient(37, 10))
# print(quotient(-33, 10))
# print(quotient(15, 5))
# print(quotient(20, 7))
