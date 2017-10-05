def primes_list(n):
    primes = []
    possible = 2
    while len(primes) != n:
        isPrime = True
        for i in range(2, possible - 1):
            if (possible % i) == 0: 
                isPrime = False
        if isPrime == True:
            primes.append(possible)
        possible += 1
    return primes

