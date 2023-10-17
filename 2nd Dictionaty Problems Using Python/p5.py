# python program to convert tuples into dictionary

# creating a function


def ofconvert(tup, di):  # taking two arguments
    di = dict(tup)

    return di


tup = [("Sachin", 10), ("Kohli", 18), ("Rohit", 45), ("Smith", 49)]

di = {}

print(ofconvert(tup, di))

# approah 2

# using dict in single line

print(dict([("Sachin", 10), ("Kohli", 18), ("Rohit", 45), ("Smith", 49)]))

# approach 3

# by using setdefault()

tup1 = [
    ("Sachin", 10),
    ("Kohli", 18),
    ("Rohit", 45),
    ("Smith", 49),
    ("Ravihandran Ashwin", 99),
]

# creating an empty dictionary

d1 = {}

# using a for loop for iteration

for key, value in tup1:
    d1.setdefault(key, value)

# printing the dictionary

print(d1)
