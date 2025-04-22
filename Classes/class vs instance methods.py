class Point:
    # a class level attribute
    default_colour = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # this is called a decorator
    # it's a way to extend the behaviour
    # of a method or function
    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


# I am calling the 'factory' settings of the class
point = Point.zero()
# I am using the draw function to print the instance values
point.draw()
