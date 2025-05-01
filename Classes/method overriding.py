class Animal:
    # this is a constructor
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")

    def fly(self):
        print("fly")


class Mammal(Animal):
    # this constructor overrid the age constructor
    def __init__(self):
        print("Mammal Constructor")
        self.weight = 2
        # this can be moved before the weight constructor
        super().__init__()

    def walk(self):
        print("walk")


m = Mammal()
print(m.age)
print(m.weight)
