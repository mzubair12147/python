'''
    str.format() : gives more control when displaying output of the string
'''

# {} are format fields and they act as a placeholder for a value or a variable.
string = "I will be {} to {} your {}"

item1 = "happy"
item2 = "fuck"
item3 = "mommy"

# print(string.format(item1, item2, item3))

# positional arguments in formatted strings
string2 = "I will be {0} to {0} your {2}"

item1 = "happy"
item2 = "fuck"
item3 = "mommy"

# print(string2.format(item1, item2, item3))


# formatting strings with keyword arguments
string3 = "I will be {reaction} to {action}"
# print(string3.format(reaction = "happy", action = "fuck your mom"))

#providing padding to the arguments to the formatted strings
string4 = 'hello {:20} you are a cocksucker'
string5 = 'hello {:<20} you are a cocksucker' # left align the argument value
string6 = 'hello {:>20} you are a cocksucker' # right align the argument value
string7 = 'hello {:^20} you are a cocksucker' # center align the argument value
# print(string4.format("Tania"))
# print(string5.format("Tania"))
# print(string6.format("Tania"))
# print(string7.format("Tania"))

# print(f"This is a formatted {"shit"}")




# formating numbers
number = 23.192789172
number2 = 1000000000
formating_numbers = "The number is: {:.2f}" # it will also round off your number
formating_numbers2 = "The number is: {:,}"
formating_numbers3 = "The number is: {:b}" # in binary
formating_numbers4 = "The number is: {:o}" # in octal
formating_numbers5 = "The number is: {:X}" # in hexa
formating_numbers6 = "The number is: {:e}" # in scientific notation
print(formating_numbers.format(number))

print(formating_numbers2.format(number2))
print(formating_numbers3.format(number2))
print(formating_numbers4.format(number2))
print(formating_numbers5.format(number2))
print(formating_numbers6.format(number2))
