'''
    tuples are similar to lists but
    Tuples are ordered and unchangable
    they are used to group related data
'''

tupe = (1,2,3,4,5,6)
print(tupe)
print(tupe.count(5))
print(tupe.index(6))

print()
for i in tupe:
    print(i)
print()

if 3 in tupe:
    print("3 is in the tuple")