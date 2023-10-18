# python program to check wheather a variable is string or not

# by using isinstance(x,str) method

# creating a variable

t1 = "Subham and Shreyoshi "

print("The original variable  is ", str(t1))

# checking wheather that variable is string or not

check = isinstance(t1, str)

print(f"Is the variable {t1} is a string  :>>", str(check))

# approach 2

# by  using type function ()

t2 = "Subham and Shreyoshi"

print("The original variable is ", str(t2))

# checking wheather that variable is stirng or not

r1 = type(t2) == str

print(f" Is the variable {t2} is  string ", str(r1))
