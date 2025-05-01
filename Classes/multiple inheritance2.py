# This is a good example of multiple inheritance
class Flyer:
    def fly(self):
        pass


# both classes are very different
class Swimmer:
    def swim(self):
        pass


# the flying fish can do two very different things
# it can fly and swim
class FlyingFish(Flyer, Swimmer):
    pass
