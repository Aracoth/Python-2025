try:
    # this will open a file. Don't forget to close it later.
    file = open("cleaning up.py")
    age = int(input("Age: "))
    xfactor = 10 / age

# only one exception can be executed
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
# finally clause is always executed. Use it to close file
finally:
    file.close()
