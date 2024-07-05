numbers = [98, 76, 59, 40, 92, 500, 0, 100]
# numbers.sort()
# print(numbers)
# numbers.sort(reverse= True)
# print(numbers)

sorted_list = sorted(numbers, reverse=True)
print(sorted_list)

students = (
    ("zeeshan", 1, 84),
    ("shahzaib", 2, 89),
    ("ahmad", 3, 36),
    ("adeel", 4, 11),
    ("sohaib", 5, 67),
    ("waris", 6, 100),
    ("manan", 7, 79),
)

marks = lambda mark: mark[2]
sorted_students = sorted(students, key=marks, reverse=True)
for i in sorted_students:
    print(i)
