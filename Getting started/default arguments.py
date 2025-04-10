# optional parameters (by=1) should come after the required parameter
def increment(number, by=1):
    return number + by


# if a second argument isn't passed, the default argument will be used
print(increment(2))
