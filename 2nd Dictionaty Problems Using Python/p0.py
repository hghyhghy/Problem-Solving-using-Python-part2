# python program  for insertion at the  beginning of the ordered list

from collections import OrderedDict

# initializing the ordereddict

dic = OrderedDict([("Shreyoshi", "2"), ("Shrestha", "3")])

# updating the dict

dic.update({"Subham": "1"})

dic.move_to_end(
    "Subham", last=False
)  # making the update at the first by using last =false

print("After operation the dictionary becomes ", str(dic))

# approach 2


dic1 = OrderedDict([("Shreyoshi", "2"), ("Shrestha", "3")])

dic2 = OrderedDict([("Subham", "1"), ("Subarna", "4")])

both = OrderedDict(list(dic2.items()) + list(dic1.items()))

# printing the list

print("The updated result is ", str(both))
