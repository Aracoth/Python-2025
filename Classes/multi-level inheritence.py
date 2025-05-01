class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")


# chickens can't fly
class Chicken(Bird):
    pass


# Employee - Person - LivingCreature - Thing
# Limit inheritence to 1, or 2 levels.
