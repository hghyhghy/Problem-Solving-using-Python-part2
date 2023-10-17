# python program to print the sum of all elements form the list

# creating a function


def ofsum(d):
    # creating an empty list

    sum = 0

    for i in d.values():
        sum = sum + i

    return sum


d = {"a": [100], "b": [200]}

print(f"The sum of the elements of the dictionary {d} is ", str(ofsum(d)))
