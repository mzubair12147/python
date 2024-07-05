class Car:
    color = None

def changeColor(car, color):
    car.color = color

car = Car()
changeColor(car,"white")
print(car.color)