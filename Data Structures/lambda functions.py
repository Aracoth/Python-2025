items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]

# lambda is an anonymous function used instead of creating a new function
items.sort(key=lambda item: item[1], reverse=True)
print(
    f"""
    Item list:

    {items[0]}
    {items[1]}
    {items[2]}

"""
)
