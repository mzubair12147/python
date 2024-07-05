# lambda functions are the function that are written in one line using lambda keyword and can accept any number of arguments. but only has one keyword
# think ofi it as a shortcut. useful if needed for a shorter period of time, throw-away

# symtax => lambda parameters: expression
# it returns a function object
mul = lambda x,y : x*y

checkAge = lambda age: True if age >= 18 else False

if checkAge(18):
    print("you can marry")
else:
    print("you are to young for marriage")