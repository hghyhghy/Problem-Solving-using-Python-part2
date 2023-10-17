# sorting the list by using lamda function


l1 = [
    {"Name": "Subham", "Age": 20},
    {"Name": "Shreyoshi", "Age": 19},
    {"Name": "Shrestha", "Age": 21},
]

# sorting the elements by age


print("The list sorted by age is :")

print(sorted(l1, key=lambda i: i["Age"]))


# sorting the   elements by age and name

print("The list sorted by age and name  is :")

print(sorted(l1, key=lambda i: (i["Age"], i["Name"])))

# sorting the   elements by age in reversed order


print("The list sorted by age and in reversed order is :")

print(sorted(l1, key=lambda i: i["Age"], reverse=True))
