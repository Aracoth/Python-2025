# this is a weird one, it's like making a tuple inside the functions parameter


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
