# counting the frequency  in a list using dictionary


import operator

# creating a function


def ofcount(l):
    # creating an empty dictionary

    d1 = {}

    # using a for loop

    for i in l:
        d1[i] = l.count(i)

    for key, values in d1.items():
        print("%d:>%d" % (key, values))


l = [1, 1, 1, 2, 2, 3, 4, 4, 5, 5, 5, 5, 9]

print(ofcount(l))
