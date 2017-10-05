def zap_buzz(x):
    mod7 = x % 7
    hundreds = x // 100 % 10
    tens = x // 10 % 10
    ones = x // 1 % 10
    contains3 = False
    if hundreds == 3 or tens == 3 or ones == 3:
        contains3 = True
    if mod7 == 0 and contains3 == True:
        return 'zap buzz'
    elif mod7 == 0:
        return 'zap'
    elif contains3:
        return 'buzz'
    return x
