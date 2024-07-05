"""
dictionary comprehension: create dictionary by using an expression
                        can replace for loops and certain lambda functions

syntax: dictionary = {key: expression for (key,value) in iterable}
"""

citiesInF = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}

citiesInC = {key: ((value - 32) * (5 / 9)) for (key, value) in citiesInF.items()}

for key, value in citiesInC.items():
    print(f"{key} : {int(value)}")

# with conditional
temperatureInCities = {key: value for (key, value) in citiesInC.items() if value > 10}
print(temperatureInCities)

tempAbstract = {
    key: "Cold" if value <= 10 else "Hot" for (key, value) in citiesInC.items()
}

print(tempAbstract)


# performing functions on values
def f_to_c(value):
    return float("{:.2f}".format((value - 32) * (5 / 9)))


newTempC = {key: f_to_c(value) for (key, value) in citiesInF.items()}
from os import system

system("cls")
print(newTempC)
