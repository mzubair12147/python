'''
duck typing: concept where the class of an object is less important
            class type is not checked if minimum attributes/methods are present
            "If it walks like a duck or it quacks like a duck then it must be a duck 
'''

class Duck:
    def walk(self):
        print('The duck is walking')

    def talk(self):
        print("The duck is qwaking")

class Chicken:
    def walk(self):
        print('The Chicken is walking')

    def talk(self):
        print("The chicken is clucking")

class Person:
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the clutter")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)