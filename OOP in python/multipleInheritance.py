# multiple inheritance: when a child class is derived from more then one parent class

class Prey:
    def flees(self):
        print("This small animal is flees")
    
class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

fish = Fish()
fish.flees()
fish.hunt()