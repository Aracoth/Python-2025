try:
    age = int(input("Age: "))
    xfactor = 10 / age
# only one exception can be executed
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
