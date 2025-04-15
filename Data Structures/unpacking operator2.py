values = list(range(5))
values = [*range(5), *"Hello"]
print(values)

first = [1, 2]
second = [3]
values2 = [*first, "a", *second, *"Hello"]
print(values2)
