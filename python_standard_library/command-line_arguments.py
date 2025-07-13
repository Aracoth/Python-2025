import sys

if len(sys.argv) == 1:
    print("USAGE: python3 command-line_arguments.py <password>")
else:
    password = sys.argv[1]
    print("Password", password)
