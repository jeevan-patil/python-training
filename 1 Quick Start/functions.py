#!/usr/bin/python3

def isPrime(n):
    if n == 1:
        print('1 is special case.')
        return False
    for x in range(2, n):
        if n % x == 0:
            print('{} equals {} X {}'.format(n, x, n // x))
            return False
    else:
        print(n, 'is a prime number.')
        return True


for num in range(1, 20):
    isPrime(num)
