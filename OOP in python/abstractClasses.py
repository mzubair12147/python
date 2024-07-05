# Abstract classes prevent a user to create an object of that class
# compels a user to overide abstract methods in a child class

# abstract class: is a class which contain one or more abstract methods
# abstract methods: a method that has a declaration but does not have an implementation.

# abc = abstract base class
from abc import ABC, abstractmethod

# creating an abstract class with an abstract method
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class shit(Vehicle):
    def start(self):
        print("Let's take a shity start")

hell = shit()
hell.start()