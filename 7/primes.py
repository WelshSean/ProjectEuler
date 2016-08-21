#!/usr/bin/python

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

def checkPrime(n):
    if n in  [0 ,1]:
        return False
    if n == 2:
        return True
    prime = True
    i = 2
    while i < n:
        if n % i == 0:
            prime = False
            break
        else:
            i += 1

    return prime

def nthPrime(n):
    prime = 0
    candidate = 0
    while True:
        if checkPrime(candidate):
            prime += 1
            if prime == n:
                return candidate
        candidate += 1


print nthPrime(6) # should be 13
print nthPrime(10001)
