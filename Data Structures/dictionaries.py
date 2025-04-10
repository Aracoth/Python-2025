point = {"x": 1, "y": 2}
# dictionaries can take keyword arguments
point = dict(x=1, y=2)
print(point)
# dictionary indexes take KEY values not numeric
print(point["x"])
# you can change a keys value
point["x"] = 10
# you can add new keys
point["z"] = 20
print(point)
# check if a key exists
if "a" in point:
    print(point["a"])
# another checking method, can choose default value
print(point.get("a", 0))
# delete key
del point["x"]

for key in point:
    print(key)
