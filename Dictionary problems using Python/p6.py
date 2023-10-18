# python program to check keys associated with values in dictionaries

from collections import defaultdict

# creating Aa dictionary

d1 = {"Subham": [1, 2, 3], "Shreyoshi": [2, 3, 5], "Shrestha": [1, 3]}

print("The original dictionary before operation is ", str(d1))

res = defaultdict(list)

for key, value in d1.items():
    for ele in value:
        res[ele].append(key)

print("The value associated with the dictionary is ", str(dict(res)))


# approach 2

# creating a dictionary

d = {"Subham": [1, 2, 3], "Shreyoshi": [2, 3, 5], "Shrestha": [1, 3]}

print("The original dictionary before operation is ", str(d))

# creating an empty  dictionary

result = {}

for key, val in d.items():
    for ele in val:
        if ele in result:
            result[ele].append(key)

        else:
            result[ele] = [key]


print("After opereation the dictionary is ", str(result))
