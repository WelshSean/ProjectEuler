#!/usr/bin/python

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
#                print "Found Prime: " + str(i) 
                break

        # pick out primes
        primes = []
        for i in numbers.keys():
            if numbers[i] == "Prime":
                primes.append(i)
       
    return primes
        
    
    

print sieve_Eratosthenes(25)
print sieve_Eratosthenes(10000)
