def down_up(n):
    palindrome = []
    for x in reversed(range(1, n + 1)):
       palindrome.append(x)
    for x in range(2, n + 1):
        palindrome.append(x)
    return palindrome
