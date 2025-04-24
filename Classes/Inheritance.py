class Animal:

    def eat(self):
        print("eat")

    def fly(self):
        print("fly")


# Animal: Parent, Base
# Mammal: Child, Sub
class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()
f = Fish().__class__.__name__
