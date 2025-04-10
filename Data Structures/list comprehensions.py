items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

prices = list(map(lambda item: item[1], items))
print(prices)
prices2 = [item[1] for item in items]
print(prices2)

filtered = list(filter(lambda item: item[1] >= 10, items))
filtered2 = [item for item in items if item[1] >= 10]
print(type(filtered2))
