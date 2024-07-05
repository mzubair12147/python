# Higher order functions will either accept functions as input or return functions as output
#                       In python functions are also treated as objects

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(function, text):
    print(function(text))

# hello(loud, "this is some text in lowercase")

def setA(a):
    def setB(b):
        return a/b 
    return setB

a = setA(100)
print(a(4))