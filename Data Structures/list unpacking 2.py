numbers = [1, 2, 3, 4, 4, 4, 4, 9]
# when you prefix a parameter with * it will pack into a list
first, second, third, *other, last = numbers
print(first, second, third, last)
# other will pack all the numbers between into one variable list
print(other)


items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]
products = [product[0] for product in items]
print(
    f"""
    {products[0]}
    {products[1]}    
    {products[2]}
"""
)
