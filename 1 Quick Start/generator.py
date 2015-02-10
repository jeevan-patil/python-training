#!/usr/bin/python3

def isPrime(n):
    if n == 1:
        #print('1 is a special case.')
        return False
    for x in range(2, n):
        if n % x == 0:
            #print('{} equals {} X {}'.format(n, x, n // x))
            return False
    else:
        #print(n, ' is a prime number.')
        return True

def primes(n = 1):
    while(True):
        if isPrime(n): yield n
        n += 1

for n in primes():
    if n > 100: break
    print(n, end = ' ')
