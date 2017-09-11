def coins(cents):
    quarters = cents // 25
    dimes = (cents % 25) // 10
    nickles = (cents % 25 % 10) // 5
    pennies = (cents % 25 % 10 % 5)
    totalCoins = quarters + dimes + nickles + pennies
    return totalCoins
