# capitalize each first letter, no spaces
class Point:
    def draw(self):
        print("draw")


# a variable of the new class
point = Point()
# __main__
print(type(point))
# is this variable an instance of this class
print(isinstance(point, Point))
