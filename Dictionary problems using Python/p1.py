# python program to remove a key from the dictionary


d = {"a": [100], "b": [200], "c": [111], "d": [210]}

print("Before removing the original dictionary is ", str(d))

# deleting a key by using del keyword

del d["b"]

print("After removing the original dictionary is ", str(d))

# approach 2

# by using pop operation

d1 = {"a": [100], "f": [200], "c": [111], "d": [210]}

print("Before removing the original dictionary is ", str(d1))

# removing a key by using pop method

removed_val = d1.pop("f")

print("After removing the original dictionary is ", str(d1))
