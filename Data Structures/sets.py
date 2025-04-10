numbers = [1, 1, 2, 3, 4]
# the set removes the duplicate numbers
first = set(numbers)
second = {1, 5}
# this creates a union of the two sets
print(first | second)
# intersection - numbers that are in both sets
print(first & second)
# get the difference between two sets
print(first - second)
# return characters that aren't in both sets
print(first ^ second)

# sets cannot be used with index because unordered

if 1 in first:
    print("yes")
