letters = ["a", "b", "c"]

# Add
letters.append("d")
# place to add and what to add
letters.insert(0, "-")

# Remove
letters.pop()
print(letters)
# removes only the first occurance of the value
letters.remove("b")
del letters[0:3]
letters.clear()
print(letters)
