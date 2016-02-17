#!/usr/bin/python

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20

def isEvDiv(testnum,n):
    for i in range(1, n+1):
        if testnum % i != 0:
            return False
    return True


#print isEvDiv(2520,10)
#print isEvDiv(2521,10)

def chkEvDiv(n):
    index = n
    while True:
        if isEvDiv(index, n):
            return index
        else:
            index += 1



print chkEvDiv(10)
print chkEvDiv(20)

 


