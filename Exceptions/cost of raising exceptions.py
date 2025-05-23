# this module let's you calculate execution time
from timeit import timeit

# raising exceptions can be slower
code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""
# using a None statement looks simpler and is faster
code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age

xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""

print("first code ", timeit(code1, number=10000))
print("second code ", timeit(code2, number=10000))
