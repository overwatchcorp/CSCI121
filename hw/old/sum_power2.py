def sum_power2(n):
    powerString = ''
    if n == 0:
        powerString += '1'
    if n >= 1:
        powerString += '(' + sum_power2(n - 1) + '+' + sum_power2(n - 1) + ')'
    return powerString

