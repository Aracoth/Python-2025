class Animal:
    # this is a constructor
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

    def fly(self):
        print("fly")


# Animal: Parent, Base
# Mammal: Child, Sub
class Mammal(Animal):
    def walk(self):
        print("walk")


# Fish has inherited: Animal class
class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()
print(m.age)
