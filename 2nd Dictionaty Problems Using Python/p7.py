# removing all duplicate words from a   given string

from collections import Counter

# creating a function to do that


def toremove(inp):
    # split the input

    inp = inp.split()

    # counting the occurances of a word by using counter

    uniq = Counter(inp)

    s = " ".join(uniq.keys())

    # printing the value of s

    print(s)


inp = "Java is good and  Python  is also good "

toremove(inp)


# approach 2

# by using if else loop

sen = "Java is good and  Python  is also good "

# spliting the  string

sen = sen.split()

# creating an empty list to store the data

k = []


# using a for loop

for i in sen:
    if sen.count(i) >= 1 and (i not in k):
        k.append(i)

# printing  the values

print(" ".join(k))

# by suing dict

# in a single line

string1 = "Java is good and  Python  is also good "

print(" ".join(dict.fromkeys(string1.split())))

# by using set

string1 = "Java is good and  Python  is also good "

print(" ".join(set(string1.split())))
