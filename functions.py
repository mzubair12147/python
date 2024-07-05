# functions: block of code whic runs ony when it is called
def greet(name = 'Gentlemen'):
    print(f"hello {name}")

# greet()
# greet("Bastard")

# for i in range(100):
#     greet()

def printTable(num, to):
    for i in range(to):
        print(f"{num} x {i+1} = {num*(i+1)}")

def calNextInTable(num, nextNum):
    return f"{num} x {nextNum} = {num * nextNum}"

# printTable(20,5)
# for i in range(10):
#     print(calNextInTable(47,i+1))



# keyword arguments in python
# in case of positional arguments the order of the arguments matters. 
# in case of keyword arguments the order matters.
# in keyword arguments the argument is precedded by an identifier when we pass them into the function. python knows the names of the arguments that our function received.
def sayHello(first = "",middle = "",last =""):
    print(f"Hello {first} {middle} {last} ")

sayHello(last="Zubair")

# nested function calls: a function call inside another function call. because some function return values, which we can immediately use as an argument to another function.
# from math import sqrt
# print("\nThe absolute number after square root and round is: " + str(round(sqrt(abs(float(input("Enter a number: ")))))) + '\n')




# The args parameter in python
    # a parameter that packs all arguments in to a tuple
    # useful so that a function can accept a varrying number of arguments
def sum(*arguments):
    print(arguments)

# sum(1,2,3,4,5,6,7,8,9)




# The kwargs parameter in python
    # parameter that will pack all arguments into a dictionary
    # useful so that a function can accept a varying amount of keyword argumetns
def hello(**person):
    print(f"Hello {person["name"]}")
    print(f"You are {person["age"]} years old")
    print(f"Your height is: {person["height"]}")
    if(person.get("gender") == "male"):
        if(person.get("cockSize")):
            print(f"Your cock size: {person.get("cockSize")} inches")
        else:
            print("You did not provide your cock size.")
    elif(person.get("gender") == "female"):
        if(person.get("boobSize")):
            print(f"Your boob size is: {person.get("boobSize")} inches")
        else:
            print("You didn't provide your boob size.")
    else:
        print("You didn't provide your gender")

hello(name = "Muhammad Zubair", age = 21, height= 5.10)