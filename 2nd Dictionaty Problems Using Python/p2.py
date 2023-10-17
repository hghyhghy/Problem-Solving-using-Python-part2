#   python peogram to sort dictionaries by using key or values

# creating a dictionart

from collections import OrderedDict

testdic = {"Errors": 4, "Fixed": 1, "Remaining": 3}

mydic = OrderedDict(sorted(testdic.items()))

print(mydic)


testdic1 = {"Errors": [10, 2, 3], "Fixed": [4, 50, 6], "Remaining": [7, 8, 9]}

print("The original dictionary is  ", str(testdic1))

rest = dict()

for key in sorted(testdic1):
    rest[key] = sorted(testdic1[key])

print("The sorted dictionary is ", str(rest))
