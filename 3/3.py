#!/usr/bin/python

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def checkPrime(n):
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
    
    

def largestPrime(number):
# Brute force - too slow
    index = number
    while True:
        print index
        if number % index == 0 and checkPrime(index):
            break
        else:
            index -= 1
  
    return index

print largestPrime(13195)
print largestPrime(600851475143)
#print checkPrime(4)
#print checkPrime(2)
#print checkPrime(3)
#print checkPrime(100)
#print checkPrime(101)
