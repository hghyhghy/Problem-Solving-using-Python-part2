# python dictionary  with keys having multiple inputs


import random as rn

# creating an empty dictionary

dic = {}

# inserting a triplet in the dictionary

x, y, z = 10, 20, 30

dic[x, y, z] = x + y - z

# inserting a triplet in the  same dictionary

x, y, z = 4, 5, 9

dic[x, y, z] = x + y - z


# printing the dictionary

print(dic)
