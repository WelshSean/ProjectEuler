#!/usr/bin/python

def sqrs(number):
    n = 1
    sqsum = 0 
    sumsq = 0
    while n <= number:
        sqsum += n
        sumsq += n*n
        n+=1
    sqsum = sqsum * sqsum
    diff = sqsum - sumsq
    print "Square of the sums (sqsum): " + str(sqsum)
    print "Sum of the sqaures (sumsq): " + str(sumsq)
    print "Diff: " + str(diff)
    return diff
   
print sqrs(10) 
print sqrs(100) 
