# this is a global variable, it is best to avoid global variables,
# it is used globally in this file
message = "a"


def greet(name):
    # this is a local variable, it is used only in this function
    message = "b"


greet("Ash")
print(message)
