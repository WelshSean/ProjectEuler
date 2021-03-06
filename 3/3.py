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

def sieve_Eratosthenes(n):
    # Find all primes <= n
    # Sieve of Eratosthenes  https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    # Build up empty dictionary of numbers all marked as Prime
    numbers = {}
    for i in range(n):
        numbers[i+1] = "Prime"

    # Now we start with 2 - the first prime
    numbers[2] = "Prime"
    p = 2
    foundPrime = True

    # Loop until we dont find any more Primes
    while foundPrime:
        # Mark multiples of prime p as composite
        for i in range(2*p, n+1, p):
            numbers[i] = "Composite"
        # Look for next prime > p, if we find one we start again, if not we're done
        foundPrime = False
        for i in range(p+1, n+1):
            if numbers[i] == "Prime":
                p = i
                foundPrime = True
                print "Found Prime: " + str(i) 
                break

        # pick out primes
        primes = []
        for i in numbers.keys():
            if numbers[i] == "Prime":
                primes.append(i)
       
    return primes
        

    
    

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

#print largestPrime(13195)
#print largestPrime(600851475143)
#print checkPrime(4)
#print checkPrime(2)
#print checkPrime(3)
#print checkPrime(100)
#print checkPrime(101)
print sieve_Eratosthenes(25)
