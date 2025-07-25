import random
import string

print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4]))
print(random.choices([1, 2, 3, 4], k=2))
# the empty string creates a string output
# a comma will separate with a comma
print("".join(random.choices(string.ascii_letters, k=4)))

print(string.ascii_letters)

numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)
