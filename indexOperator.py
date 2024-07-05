#index operator []

name = "Muhammad Zubair"

# if name[0] == name[0].lower():
#     print("The first character of the name is lowercase")
# else : 
#     name = name.capitalize()

first_name = name[:8].upper()
last_name = name[9:].upper()
print(first_name + ' ' + last_name)