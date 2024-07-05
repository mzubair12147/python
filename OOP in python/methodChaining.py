# method chaining : calling multiple methods sequentially
#                   each call performs an action on the same object and return self

class Animal:
    alive = True

    def run(self):
        print("Animal is running")
        return self
    
    def stop(self):
        print("Animal is stopped")
        return self
    
    def eat(self):
        print("Animal is eating")
        return self
    
    def drink(self):
        print("Animal is drinking water.")
        return self

anima = Animal()
anima.run().stop().eat().drink()