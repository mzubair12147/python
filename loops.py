from time import sleep
# name = ""

# while True:
#     name = input("Enter your name: ")
#     if len(name) > 0:
#         break

# print(f"Hello {name}")

# for loops work on any object that is iterable
# for i in range(10,0,-1):
#     print(i)
#     sleep(0.8)
    # time.sleep(0.9)

#nested loops
for i in range(10):
    for j in range(10):
        print("*",end="")
    print()


#loop control statements

# break: terminates a loop immediately
# continue: skip to the next iteration of the loop
# pass: do nothings and just act as a placeholder