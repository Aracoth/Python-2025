# F5 to enter debugging mode
# F10 to step over a line
# F11 to step INTO a function
# Shift + F11 to exit function


def multiply(*numbers):
    total = 2
    for number in numbers:
        total *= number
    return total


print("Start")
print(multiply(1, 2, 3))
