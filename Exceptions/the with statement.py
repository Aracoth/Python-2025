try:
    # the WITH statement will automatically call file.close
    # it can only be used on objects with the .__enter__. method
    # you can add another file as a second argument
    with open("cleaning up.py") as file, open("another.txt") as target:
        print("File opened.")
        file.__
    age = int(input("Age: "))
    xfactor = 10 / age

# only one exception can be executed
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
