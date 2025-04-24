class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # This function adds the two values together
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(10, 20)
other = Point(1, 2)
# this variable stores the added value
combined = point + other
# this prints the value of x, which is 'other'
print(combined.x)
