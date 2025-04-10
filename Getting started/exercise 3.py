number = int(input("Type your number here "))


def fizz_buzz(Input):
    if (number % 3 == 0) and (number % 5 == 0):
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


fizz_buzz(number)
