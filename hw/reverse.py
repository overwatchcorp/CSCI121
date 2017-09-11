def reverse(x):
    thousands = x % 10000 // 1000
    hundreds = x % 1000 // 100
    tens = x % 100 // 10
    ones = x % 10 // 1
    reversedInt = (ones * 1000) + (tens * 100) + (hundreds * 10) + thousands 
    if thousands == 0:
        return reversedInt // 10
    return reversedInt 
