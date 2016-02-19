#!/usr/bin/python

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 
# (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


def num2words(num):
    unitlookup = { 1 : "one",
                   2 : "two",
                   3 : "three",
                   4 : "four",
                   5 : "five",
                   6 : "six",
                   7 : "seven",
                   8 : "eight",
                   9 : "nine",
                  10 : "ten",
                  11 : "eleven",
                  12 : "twelve",
                  13 : "thirteen",
                  14 : "fourteen",
                  15 : "fifteen",
                  16 : "sixteen",
                  17 : "seventeen",
                  18 : "eighteen",
                  19 : "nineteen"}

    tenlookup = { 2 : "twenty",
                  3 : "thirty",
                  4 : "forty",
                  5 : "fifty",
                  6 : "sixty",
                  7 : "seventy",
                  8 : "eighty",
                  9 : "ninety"}

    numstring = ""

    thousands =  num // 1000 
    thousandTemp =  num % 1000 

    # Add string for thousands
    if thousands != 0:
        numstring = numstring + unitlookup[thousands]  + " thousand "

    hundreds = thousandTemp // 100
    hundredTemp = thousandTemp % 100
    
    # Add string for hundreds
    if hundreds != 0:
        numstring = numstring + unitlookup[hundreds]  + " hundred "

    # Add the string and if we have hundreds or thousands AND we have tens or units :-)
    if (hundreds != 0 or thousands != 0) and hundredTemp !=0:
        numstring = numstring + "and " 

    # Deal with where we have <20 left (irregular numbers)
    if hundredTemp != 0 and hundredTemp < 20:
        numstring = numstring  + unitlookup[hundredTemp] 

    # deal with regular tens 
    if hundredTemp != 0 and hundredTemp >= 20:
        tens = hundredTemp // 10
        units = hundredTemp % 10

        numstring = numstring +  tenlookup[tens] 
       
        # Deal with units where we have tens (hyphenate) 
        if units !=0 and tens !=0:
            numstring = numstring + "-" + unitlookup[units]
    
        # Deal with units where we dont have tens (no hyphenation)
        if units !=0 and tens == 0:
            numstring = numstring +  unitlookup[units]
        
      
    return numstring

#for test in [1000, 1100, 1200, 1213, 1250, 1254, 1209, 1, 27, 100, 10, 109, 127]:
#    print test, num2words(test)


def countLetters(string):
    count = 0
    for i in string:
       if i not in [" ", "-"]:
           count +=1

    return count

#for test in ["five", " five", " five ", "five-five", "-five", " -five" ]:
#    print test, countLetters(test)


def countNumList(n):
    chars = 0
    for i in range(1, n+1):
        chars += countLetters( num2words(i) )

    return chars

# print countLetters( num2words(342) )
# print  num2words(342) 

# print countLetters( num2words(115) )

print countNumList(5)
print countNumList(1000)
