"""
    zip(*iterable) : the zip function will aggregate two or more iterables  and creates a zip object with paired elements stored in tuples for each element in the zip object
"""

userName = ["iqboy", "shadow", "boy"]
passwords = ["password", "abc123", "guest"]
gender = ["male" for i in range(3)]

# note: zip objects are iterable
users = zip(userName, passwords, gender)
for i in users:
    print(i)
