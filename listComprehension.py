"""
list comprehensions : A way to create a new list with less syntax
can mimic certain lambda functions, easier to read 
formula : 
    list = [expression for item in iterable]
    list = [expression for item in iterable if conditional]
"""

squared = []
# for i in range(1, 11):
#     squared.append(i * i)

squared = [i * i for i in range(1, 11)]

# print(squared)

# miic lambda functions
students = [i for i in range(100, 0, -10)]

student_passed = list(filter(lambda marks: marks > 50, students))

print(student_passed)

# doing the same with lambda like list comprehension

student_passed_2 = [i for i in students if i > 50]
print(student_passed_2)

# for multiple outputs
student_passed_3 = [i if i >= 50 else "failed" for i in students]
print(student_passed_3)
