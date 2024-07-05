from car import Car

car1 = Car('Honda' , 'Honda City', 2022, 'white')
car2 = Car('Tesla', 'Tesla X', 2022, 'red' )

# print(car2.make)
# print(car2.model)
# print(car2.year)
# print(car2.color)

# car2.drive()
# car2.stop()

car1.wheels = 6

print("\nBefore changing class variable values.")
print(car1.wheels)
print(car2.wheels)
print(Car.wheels)

Car.wheels = 2

print("\nAfter changing class variable values.")
print(car1.wheels)
print(car2.wheels)
print(Car.wheels)