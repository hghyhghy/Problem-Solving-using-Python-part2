# convert  string to bytes

# creating a string first

string = "Subham And Shreyoshi Love Each other "

print("The original string is ", str(string))

# converting the string to bytes

res = bytes(string, "utf-8")

print(f"The type of {string}  is  ", str(type(res)))

# approach 2

# by using encode

s = "Subham And Shreyoshi Love Each other "

print("The original string is ", str(s))

r = s.encode("utf-8")

print(f"The type of {s}  is  ", str(type(r)))
