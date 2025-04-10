items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]
# the filter function lets me filter using comparison operators
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)
