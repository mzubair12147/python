# multi Level Inheritance : when a derived class inherits ffom another derived class

class Organisms:
    alive = True

class Animal(Organisms):
    # Organism class is inherited
    def eat(self):
        print("This animal is eating")
    
    def sleep(self):
        print("This animal is sleeping")

class Dog(Animal):
    def bark(self):
        print("This dog is barking")

class Rabbit(Animal):
    # Animal class is inherited
    def run(self):
        print("This rabbit is running")

class Fish(Animal):
    # Animal class is inherited
    def swimming(self):
        print("This fish is swimming")

class Hawk(Animal):
    # Animal class is inherited
    def fly(self):
        print("This hawk is flying")

dog = Dog()
print(dog.alive)