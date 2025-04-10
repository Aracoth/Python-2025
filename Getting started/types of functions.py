def greet(name):
    print(f"Hi {name}")


# function types
# 1 - Perform a task
# 2 - return a value


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Ash")
file = open("content.txt", "w")
file.write(message)
