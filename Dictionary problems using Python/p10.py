# python program to  count words in a sentence

# creating a string first

t1 = "Subham and Shreyoshi "

# spliting the string

t1 = t1.split()

print(f"The no of words present in the string{t1} is ", len(t1))

# iterate over characters of a string in python

t = "SubhamandShreyoshi "

# using a for loop

for ele in t:
    print(ele, end=" ")


# using enumerator
d = "SubhamandShreyoshi "

for i, v in enumerate(d):
    print(v)
