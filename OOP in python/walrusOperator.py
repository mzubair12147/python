# walrus operator :=

# it is an assignment expression aka walrus operator
# assigns values to variables as part of a larager expressions

# name = "Bitch"
# print(name)

print(age := 21)
# print(age)

friends = list()
# while True:
#     friend = input("Enter your friend: ")
#     if friend == 'quit':
#         break
#     friends.append(friend)

while friend  := input("Enter your friend name: ") != 'quit':
    friends.append(friend)