# handling missing keys using python


# creating a dictionary


testdic = {"Errors": 4, "Fixed": 1, "Remaining": 3}

print("The value associated with Problems are ")

print(testdic["Problems"])

testdic1 = {"Errors": 4, "Fixed": 1, "Remaining": 3}

# using a if else loop

if "q" in testdic1:
    print(testdic1["Problems"])

else:
    print("Key not found")
