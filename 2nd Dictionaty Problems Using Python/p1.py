# append dictionaty keys and values using python


# creating a dictionary first

from itertools import chain  # chain is used for concatenation

testdic = {"Errors": 4, "Fixed": 1, "Remaining": 3}

print("The dictionary before operation is ", str(testdic))

rest = list(testdic.keys()) + list(testdic.values())

print("After operation the dictionary will become ", str(rest))

# approach 2

testdic1 = {"Errors": 3, "Fixed": 1, "Remaining": 3}

print("The dictionary before operation is ", str(testdic1))

res = list(chain(testdic1.keys(), testdic1.values()))

print("After operation the dictionary will become ", str(res))

# approach 3


testdic2 = {"Errors": 3, "Fixed": 1, "Remaining": 3}

print("The dictionary before operation is ", str(testdic2))

a = list(testdic2.keys())

b = list(testdic2.values())

# extending the value of b to a

a.extend(b)

# storing the value of a to a temp variable

temp = a

print("The dictionary before operation is ", str(temp))
