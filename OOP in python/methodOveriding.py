# method overiding: in method overriding a child class provides a specific implementation of a method that is already provided by the parent class.

class Animal:
    alive = True
    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    # Animal class is inherited
    def run(self):
        print("This rabbit is running")

    def eat(self):
        print("rabbit is eating a carrot.")    

class Fish(Animal):
    # Animal class is inherited
    def swimming(self):
        print("This fish is swimming")

class Hawk(Animal):
    # Animal class is inherited
    def fly(self):
        print("This hawk is flying")

# an object first tries to access a method that is more closly associated with itself before relying on a method that is provided by the parent class.
rabbit = Rabbit()
rabbit.eat()