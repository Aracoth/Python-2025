# a bad example of multiple inheritance
class Employee:
    def greet(self):
        print("Employee Greet")


# both classes have a similar function: greet
class Person:
    def greet(self):
        print("Person Greet")


# multiple inheritance can be bad, if used wrongly
# some subclasses can end up with the wrong inheritances
class Manager(Employee, Person):
    pass


manager = Manager()
# manager class will check for a greet function
# secondly: it will check it's first inheritance class
# first inherited class: Employee
manager.greet()
