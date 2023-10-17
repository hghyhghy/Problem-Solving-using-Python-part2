# sorting list of dictionaries by values  using python

from operator import itemgetter

l1 = [
    {"Name": "Subham", "Age": 20},
    {"Name": "Shreyoshi", "Age": 19},
    {"Name": "Shrestha", "Age": 21},
]

# printing the list sorted by age

print("The list sorted by age is :")

print(sorted(l1, key=itemgetter("Age")))

# sorted by name and age

print("The list sorted by age and name  is :")

print(sorted(l1, key=itemgetter("Age", "Name")))

# sorted by age but in ascending order

print("The list sorted by age and reversed  order  is :")

print(sorted(l1, key=itemgetter("Age"), reverse=True))
