# scope : A region where a variable is recognized
#         A variable is only available inside the region it is created
#         A globaly and localy scoped version of a variable can be created


# global variables are available outside all the functions and have a global scope and are available inside and outside the functions. 
name = "My name"

def display_name():
    # a variable inside a function is a local variable because the scope of the variable is local to that function.
    name = "Muhammad Zubair"
    print(name)

display_name()
print(name)

'''
    sequence of python to access a variable value
    L = local
    E = enclosing
    G = global
    B = builtin
'''