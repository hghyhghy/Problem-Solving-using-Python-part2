# python program to print unique dictionary values

# creating a dictionary first

test = {"Id": [101, 102, 103], "Ëxperience": [3, 4, 6], "Age": [23, 32, 34]}

# printing the original dictionary

print("The original dictionary is ", str(test))

# ectracting the unique values of dictionary

rest = list(sorted({ele for val in test.values() for ele in val}))

print("After sorting the elements will be ", str(rest))


# approach 2

# by using loops


xy = {"Age": [23, 34, 45], "Id": [111, 102, 121]}

print("The original dictionary is ", str(xy))

x = list(xy.values())


# creating an empty list

y = []

rest = []

# using a for loop

for i in x:
    y.extend(i)


for i in y:
    if i not in rest:
        rest.append(i)

rest.sort()


print("The modified values of the dictionary is ", str(rest))

