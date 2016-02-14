#!/usr/bin/python

# A palindromic number reads the same both ways. The largest palindrome 
# made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def isPalindrome(n):
    n = str(n)
    reversed = ""   
    for i in range (1, len(n) + 1):
        reversed = reversed + n[-i]
    if n == reversed:
        return True
    else:
        return False

def findPal():
    palindromes = []
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            product = i * j
            if isPalindrome(product):
                palindromes.append(product)
    palindromes.sort()
    return palindromes[-1]


print findPal()

#print isPalindrome(3456)
#print isPalindrome(14841)
