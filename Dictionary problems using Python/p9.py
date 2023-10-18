# split string into a list of characters

t1 = "Subham"

print([*t1])

# approach 2

# by using for loop

t = "Subham and Shreyoshi "

# creating an empty list

l = []

for letters in t:
    l.append(letters)

print(l)

# approach 3

# by using list comprehension

t0 = "Subham and Shreyoshi "

l1 = [x for x in t0]

print(l1)


# approach 4

# by creating a function


def ofsplit(words):
    return list(words)


words = "Virat Kohli"

print(ofsplit(words))
