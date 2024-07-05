# a dictionary is a changable, unordered, unique: key/value pair 
# they are fast because they use hashing, allow us to access a value quickly

capitals = {
    'USA': "Washinigton DC",
    'Pakistan': 'Karachi',
    'India': 'New delhi',
    'China': 'Beijing',
    'Russia': 'Moscow',
    'Japan':'Tokyo',
    'South Korea': 'Seol'
}

print(capitals['Japan'])

# getting a value of a key which do not exist in the capitals
# it will throw an error and disturb the normal flow of the program
# print(capitals['Canada'])

#a much safer way to access the elements that are not present in the dictionary is to use the get method
print(capitals.get('Australlia'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

capitals.update({'Germany':'Berlin'})
capitals["France"] = "Paris"

# updating the existing values
capitals.update({'USA':'New York'})
capitals['Pakistan'] = 'Islamabad'

capitals.pop('India')

print()
for key, value in capitals.items():
    print(f"key: {key},\t value: {value}")
print()

capitals.clear()