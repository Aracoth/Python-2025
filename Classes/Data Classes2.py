# a simpler form of data classes is named tuples
from collections import namedtuple

# best if class has no methods: only data
Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
print(p1.x)
# cannot mutate the values
p1.x = 10
# must create new point to change value
p1 = Point(x=10, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)
