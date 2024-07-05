class Car:
    # class variables
    # declared inside the class but outside the constructors and methods and belong to the class. also called default values for all instances of the class
    wheels = 4

    def __init__(self, make, model, year, color):
        # instance variables
        # declared inside the constructor and are given unique values
        # unique/belong to instance
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print(f"{self.model} is driving")

    def stop(self):
        print(f"{self.model} is stopped")