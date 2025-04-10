point = (1, 2) + (3, 4)
print(point)
point2 = (1, 2) * 3
print(point2)
# convert a list to a tuple
point3 = tuple([1, 2])
print(point3)
# convert a string to a tuple
point4 = tuple("Don't stand there!")
print(point4)
# access individual items using an index
point5 = (1, 2, 3)
print(point5[0])
print(point5[0:2])
# you can unpack tuples
x, y, z = point5
print(
    f"""
    x = {x}
    y = {y}
    z = {z}
"""
)
if 10 in point5:
    print("exists")
