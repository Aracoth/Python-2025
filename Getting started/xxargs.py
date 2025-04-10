# this one is like making a dictionary inside of a function


def save_user(**user):
    print(user["id"])
    print(user["name"])
    print(user["age"])


save_user(id=1, name="Ash", age=33)
