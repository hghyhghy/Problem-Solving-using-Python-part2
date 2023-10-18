# python program to check wheather a we can recreat  the first string by rearranging
# and deleting some characters from the second one

from collections import Counter

# creating a function


def ofcheck(str1, str2):
    # counting the characters by using counter  and store it in a dictionary

    dic1 = Counter(str1)

    dic2 = Counter(str2)

    # take intersections of two dictionaries

    result = dic1 & dic2

    return result == dic1


dic1 = "Subham"
dic2 = "Sdubqahham"

if ofcheck(dic1, dic2) == True:
    print("Possible ")
else:
    print("Not Possible ")
