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


print isPalindrome(3456)
print isPalindrome(14841)
