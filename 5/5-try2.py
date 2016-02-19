#!/usr/bin/python

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20

 
def findUniqFactors(n):
    """ Given a sequence of numbers from 1....n+1, find the subset of numbers who have no smaller factors """
    numlist = range(1, n+1)
    index = len(numlist) - 1
    while index > 0:
        dellist = []
        for j in range(index - 1, 0, -1):
            if numlist[index] % numlist[j] == 0:
               dellist.append(j)
        for ii in dellist:
           del numlist[ii]
        if len(dellist) != 0:
            index = len(numlist) - 1
        else:
            index -= 1
    return numlist

def isEvDiv(testnum,n):
    for i in findUniqFactors(n) :
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
#print findUniqFactors(10)
#print findUniqFactors(20)
 


