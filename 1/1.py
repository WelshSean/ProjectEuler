#!/usr/bin/python

# If we list all the natural numbers below 10 that are multiples of 
# 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def multiples(n):
    multiples = []
    sum = 0
    print n
    for i in range(1,n):
	print i
        if i % 3 == 0 or i % 5 == 0:
            multiples.append(i) 
            sum = sum + int(i)
    print "multiples :" + str(multiples)
    print "sum: " + str(sum)
            



if __name__ == "__main__":
	multiples(10)
	multiples(1000)
