# all classes are instances of the object class
# this is by default in Python


class Animal:
    # this is a constructor
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

    def fly(self):
        print("fly")


class Mammal(Animal):
    def walk(self):
        print("walk")


m = Mammal()
# is m an instance of Mammal?
print(isinstance(m, Mammal))
# is m an instance of Animal?
print(isinstance(m, Animal))
# is m an instance of object?
print(isinstance(m, object))
# all classes inherit methods from the object class
o = object()
# is Mammal a subclass of Animal
print(issubclass(Mammal, Animal))
