# Super(): method gives access to the methods of a parent class.
#          Returns a temporary object of a parent class when used


class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length=length, width= width)

class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length=length, width= width)
        self.height = height

    def area(self):
        return self.length * self.height * self.width


square = Square(3,3)
cube = Cube(3,3,3)

print(square.area())
print(cube.area())