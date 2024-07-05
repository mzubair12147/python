# string  slicing
string = "This is a string for slicing"
# [ start (inclusive) : stop (exclusive) : step ]
print(string[:10])
print(string[-7:])

# reversed string
print(string[::-1])


# slicing with slice() object and it is reusable
website = 'http://www.google.com'

slice_obj = slice(11,-4)

print(website[slice_obj])

