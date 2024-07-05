def hello():
    print("Hello! I am human")

hi = hello
hi()
# memory address of the function will be displayed!
del(hello)
try:
    print(hello)
except NameError :
    print("Function do not exists")
else:
    hello()

say = print

say("Oh I can't believe this works")