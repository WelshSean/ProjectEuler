#!/usr/bin/python

import math

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


def HPF(n):
    # Find Highest Primw Factor of n
    # Starting from 2 divide by successively larger numbers
    # to find highest factor and then work down until one is prime.
    factors = []
    divisor = 2
    
    while divisor < math.sqrt(n):
        if n % divisor == 0:
            j = n // divisor
            print "Divisor: " + str(divisor) +"Factor: " + str(j)
            # check new factor
            if checkPrime(j):
                print str(j) + " Is prime"
                factors.append(j)
            else:
                print str(j) + " Isnt prime"
            # Also check divisor. it by necessity is also a factor
            if checkPrime(divisor):
                print str(divisor) + " Is prime"
                factors.append(divisor)
            else:
                print str(divisor) + " Isnt prime"
        divisor +=1
    return factors    

print HPF(13195)
print
print
print HPF(600851475143)
         
