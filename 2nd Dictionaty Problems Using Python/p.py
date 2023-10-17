# python program to convert key value pair to flat dictionary

from itertools import product

# creating a dictionary first

dic1 = {"Month": [1, 2, 3], "Name": ["January", "February", "March"]}

# printing the original dictionary

print("The original dictionary before operation is ", str(dic1))


rest = dict(zip(dic1["Month"], dic1["Name"]))

print("The flattened dictionary is ", str(rest))


# approach 2

# by using for loop

dic2 = {"Month": [1, 2, 3], "Name": ["January", "February", "March"]}

print("The original dictionary before operation is ", str(dic2))

# using for loop

# creating a empty list

res = []

for i in range(len(dic2["Month"])):
    res[dic2["Month"][i]] = dic2["Name"][i]


print("The flattened dictionary is ", str(res))
