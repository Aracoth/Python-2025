class Point:
    # a class level attribute
    default_colour = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


# I am changing the colour within the class, not an instance
# a class level attribute
Point.default_colour = "yellow"

point = Point(1, 2)

# default_colour is defined within the class
print(point.default_colour)
print(Point.default_colour)
point.z = 10
point.draw()

# these are instances, and can have different values
another = Point(3, 4)
print(another.default_colour)
another.draw()
# another instance of Point
point = Point(0, 0)
# not currently working
point = Point.zero()
