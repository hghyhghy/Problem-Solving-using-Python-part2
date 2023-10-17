# python program to merge two dictionaries

# creating a function


def ofmerge(d, d1):
    return d.update(d1)


d = {"a": 10, "b": 11}

d1 = {"a1": 20, "b1": 21}

print(ofmerge(d, d1))

print(d)

# approach 2

# by using **

# a fucntion


def merge(di, dic):
    res = {**di, **dic}

    return res


di = {"a": 10, "b": 11}

dic = {"a1": 20, "b1": 21}

dic3 = merge(di, dic)

print(dic3)

# approach 3

# by using  | operator

# function


def ofm(d3, d4):
    rest = d3 | d4

    return rest


d3 = {"a": 10, "b": 11}

d4 = {"a1": 20, "b1": 21}

d5 = ofm(d3, d4)

print(d5)

# approach 4

# by using for loop

# a function


def tom(d6, d7):
    for i in d6:
        d7[i] = d6[i]

    return d7


d6 = {"a": 10, "b": 11}

d7 = {"a1": 20, "b1": 21}

d8 = tom(d6, d7)

print(d8)
