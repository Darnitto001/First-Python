#A program to check whether a year is a leap year or not
import re

year = 2010
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))
elif (year % 4 == 0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))


#A program to check whether a letter is a consonant or a vowel
letter = 'a'
if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print("it is a vowel")
else:
    print("it is a consonant")

