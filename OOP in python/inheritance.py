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

class Fish(Animal):
    # Animal class is inherited
    def swimming(self):
        print("This fish is swimming")

class Hawk(Animal):
    # Animal class is inherited
    def fly(self):
        print("This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
print(fish.alive)
print(hawk.alive)

rabbit.run()
fish.swimming()
hawk.fly()